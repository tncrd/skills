#!/usr/bin/env python3
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "arxiv",
#   "semanticscholar",
#   "pymupdf",
#   "pdfplumber",
# ]
# ///
"""Paper search, citation tools, and local literature index for ML research."""

import html.parser
import io
import os
import re
import sys
import textwrap
import time
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

try:
    import arxiv
except ImportError:
    sys.exit("Missing dependency: pip install arxiv")

try:
    from semanticscholar import SemanticScholar
except ImportError:
    sys.exit("Missing dependency: pip install semanticscholar")

S2_API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")


# ── Helpers ───────────────────────────────────────────────────────────────────

def get_s2():
    return SemanticScholar(api_key=S2_API_KEY) if S2_API_KEY else SemanticScholar()


def safe_s2_call(func, *args, **kwargs):
    for attempt in range(3):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if "429" in str(e) or "Too Many Requests" in str(e):
                wait = (attempt + 1) * 5
                print(f"  Rate limited. Waiting {wait}s... ({attempt+1}/3)", file=sys.stderr)
                if not S2_API_KEY:
                    print("  Tip: set SEMANTIC_SCHOLAR_API_KEY", file=sys.stderr)
                time.sleep(wait)
            else:
                print(f"  Error: {e}", file=sys.stderr)
                return None
    print("  Failed after 3 attempts.", file=sys.stderr)
    return None


def fmt_paper(title, authors, year, abstract, url, venue=None, citations=None):
    lines = [
        f"  {title}",
        f"  {', '.join(authors[:3])}{'...' if len(authors) > 3 else ''} ({year})",
    ]
    if venue:
        lines.append(f"  Venue: {venue}")
    if citations is not None:
        lines.append(f"  Citations: {citations}")
    lines.append(f"  {url}")
    if abstract:
        wrapped = textwrap.fill(abstract[:300], width=80, initial_indent="  ", subsequent_indent="  ")
        lines.append(wrapped + ("..." if len(abstract) > 300 else ""))
    return "\n".join(lines)



class _TextExtractor(html.parser.HTMLParser):
    """Extract readable text from arXiv HTML, preserving math as LaTeX."""
    SKIP_TAGS = {"script", "style", "nav", "header", "footer", "button"}
    BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "li", "section", "tr"}
    STOP_SECTIONS = {"references", "bibliography", "acknowledgements", "acknowledgments"}

    def __init__(self):
        super().__init__()
        self.text = []
        self._skip = 0
        self._current = []
        self._stopped = False

    def handle_starttag(self, tag, attrs):
        if self._stopped:
            return
        if tag in self.SKIP_TAGS:
            self._skip += 1
            return
        if tag == "math":
            attrs_dict = dict(attrs)
            alttext = attrs_dict.get("alttext", "").strip()
            display = attrs_dict.get("display", "inline")
            if alttext:
                fmt = f"$${alttext}$$" if display == "block" else f"${alttext}$"
                self._current.append(fmt)
            self._skip += 1
            return
        if tag in self.BLOCK_TAGS and self._current:
            chunk = " ".join(self._current).strip()
            if chunk:
                self.text.append(chunk)
            self._current = []

    def handle_endtag(self, tag):
        if tag in self.SKIP_TAGS or tag == "math":
            self._skip = max(0, self._skip - 1)

    def handle_data(self, data):
        if self._stopped or self._skip > 0:
            return
        stripped = data.strip()
        if not stripped:
            return
        if stripped.lower() in self.STOP_SECTIONS:
            self._stopped = True
            return
        self._current.append(stripped)

    def get_text(self):
        if self._current:
            self.text.append(" ".join(self._current).strip())
        return "\n\n".join(t for t in self.text if len(t) > 20)


def _fetch_html(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "papers.py/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def _download_pdf_bytes(arxiv_id):
    """Download PDF and return raw bytes."""
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "papers.py/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.read(), None
    except Exception as e:
        return None, str(e)


def _text_from_pdf_bytes(pdf_bytes):
    """Extract text using PyMuPDF (primary) or pdfplumber (fallback)."""
    # PyMuPDF — better text quality, handles ligatures and fonts well
    try:
        import fitz
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        pages = [page.get_text() for page in doc]
        text = "\n\n".join(p for p in pages if p.strip())
        if text:
            return text, "PyMuPDF", doc
    except ImportError:
        pass
    except Exception:
        pass

    # pdfplumber fallback
    try:
        import pdfplumber
        pages = []
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                t = page.extract_text(x_tolerance=2, y_tolerance=2)
                if t:
                    pages.append(t)
        text = "\n\n".join(pages)
        return text, "pdfplumber", None
    except ImportError:
        pass

    return None, "no PDF library available", None


def _toc_from_pdf_bytes(pdf_bytes):
    """Extract TOC from PDF bookmarks using PyMuPDF. Returns list of (level, title, page) or None."""
    try:
        import fitz
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        toc = doc.get_toc()  # [(level, title, page), ...]
        return toc if toc else None, doc
    except ImportError:
        return None, None
    except Exception:
        return None, None


def _extract_pdf(arxiv_id):
    """Legacy wrapper for read() — returns (text, error)."""
    pdf_bytes, err = _download_pdf_bytes(arxiv_id)
    if not pdf_bytes:
        return None, f"Could not download PDF: {err}"
    text, source, _ = _text_from_pdf_bytes(pdf_bytes)
    return text, None if text else "extraction failed"


def search(query, limit=10):
    """Search papers via Semantic Scholar."""
    sch = get_s2()
    results = safe_s2_call(sch.search_paper, query, limit=limit, fields=[
        "title", "authors", "year", "abstract", "url",
        "venue", "citationCount", "externalIds"
    ])
    if not results:
        print("No results found.")
        return
    count = 0
    try:
        for i, paper in enumerate(results):
            if i >= limit:
                break
            aid = (paper.externalIds or {}).get("ArXiv", "")
            authors = [a.name for a in (paper.authors or [])]
            print(f"\n[{i+1}] {aid}")
            print(fmt_paper(
                paper.title or "Untitled", authors, paper.year or "?",
                paper.abstract, paper.url or "",
                venue=paper.venue, citations=paper.citationCount
            ))
            count += 1
    except Exception:
        pass
    print(f"\n--- {count} results for: {query} ---")


def fetch(arxiv_id):
    """Fetch abstract + metadata from arXiv."""
    arxiv_id = arxiv_id.replace("https://arxiv.org/abs/", "").replace("https://arxiv.org/pdf/", "")
    client = arxiv.Client()
    results = list(client.results(arxiv.Search(id_list=[arxiv_id])))
    if not results:
        print(f"Paper not found: {arxiv_id}")
        return
    p = results[0]
    print(f"\nTitle: {p.title}")
    print(f"Authors: {', '.join(a.name for a in p.authors)}")
    print(f"Published: {p.published.strftime('%Y-%m-%d')}")
    print(f"Updated: {p.updated.strftime('%Y-%m-%d')}")
    print(f"Categories: {', '.join(p.categories)}")
    print(f"URL: {p.entry_id}")
    print(f"PDF: {p.pdf_url}")
    print(f"\nAbstract:\n{textwrap.fill(p.summary, width=80)}")


def read(arxiv_id, max_chars=150000):
    """Fetch full paper text. Tries arXiv HTML then pdfplumber PDF."""
    arxiv_id = arxiv_id.replace("https://arxiv.org/abs/", "").replace("https://arxiv.org/pdf/", "")
    base_id = arxiv_id.split("v")[0] if "v" in arxiv_id.split("/")[-1] else arxiv_id

    raw = _fetch_html(f"https://arxiv.org/html/{base_id}")
    if raw and len(raw) > 2000:
        source = "arXiv HTML"
        parser = _TextExtractor()
        parser.feed(raw)
        text = parser.get_text()
    else:
        print("No HTML. Extracting from PDF (equations may be garbled)...")
        pdf_bytes, err = _download_pdf_bytes(base_id)
        if not pdf_bytes:
            print(f"Failed: {err}")
            return
        # Try PyMuPDF with page markers
        try:
            import fitz
            doc = fitz.open(stream=pdf_bytes, filetype="pdf")
            pages = []
            for i, page in enumerate(doc, start=1):
                t = page.get_text()
                if t.strip():
                    pages.append(f"--- p.{i} ---\n{t}")
            text = "\n\n".join(pages)
            source = "PDF/PyMuPDF"
        except ImportError:
            text, _ = _text_from_pdf_bytes(pdf_bytes)[0], None
            source = "PDF/pdfplumber"
        if not text:
            print("Extraction failed.")
            return

    if len(text) < 500:
        print("Extracted content too short.")
        return

    if len(text) > max_chars:
        text = text[:max_chars]
        cut = text.rfind("\n\n")
        if cut > max_chars * 0.8:
            text = text[:cut]
        text += f"\n\n[... truncated at {max_chars:,} chars]"

    print(f"Source: {source}")
    print(f"Length: {len(text):,} chars\n")
    print(text)


def bibtex(arxiv_id):
    """Get BibTeX via Semantic Scholar."""
    arxiv_id = arxiv_id.replace("https://arxiv.org/abs/", "").replace("https://arxiv.org/pdf/", "")
    sch = get_s2()
    paper = safe_s2_call(sch.get_paper, f"ArXiv:{arxiv_id}", fields=[
        "title", "authors", "year", "venue", "externalIds", "citationStyles"
    ])
    if not paper:
        print(f"Paper not found: {arxiv_id}")
        return
    if hasattr(paper, "citationStyles") and paper.citationStyles:
        bib = getattr(paper.citationStyles, "bibtex", None)
        if bib:
            print(bib)
            return
    authors = " and ".join(a.name for a in (paper.authors or []))
    key = f"{(paper.authors[0].name.split()[-1] if paper.authors else 'unknown').lower()}{paper.year or ''}"
    doi = (paper.externalIds or {}).get("DOI", "")
    print(f"@article{{{key},")
    print(f"  title = {{{paper.title}}},")
    print(f"  author = {{{authors}}},")
    print(f"  year = {{{paper.year}}},")
    if paper.venue:
        print(f"  journal = {{{paper.venue}}},")
    if doi:
        print(f"  doi = {{{doi}}},")
    print(f"  note = {{arXiv:{arxiv_id}}}")
    print("}")


class _SectionExtractor(html.parser.HTMLParser):
    """Parse arXiv HTML into named sections."""
    HEADING_TAGS = {"h1", "h2", "h3", "h4"}
    SKIP_TAGS    = {"script", "style", "nav", "header", "footer", "button"}
    BLOCK_TAGS   = {"p", "li", "tr", "section", "div"}
    STOP_SECTIONS = {"references", "bibliography", "acknowledgements", "acknowledgments"}

    def __init__(self):
        super().__init__()
        self._skip = 0
        self._in_heading = False
        self._heading_level = 0
        self._current_heading = []
        self._current_content = []
        self._current_block = []
        self.sections = []   # list of (level, title, content)
        self._stopped = False

    def _flush_block(self):
        chunk = " ".join(self._current_block).strip()
        if chunk:
            self._current_content.append(chunk)
        self._current_block = []

    def _flush_section(self):
        title = " ".join(self._current_heading).strip()
        content = "\n\n".join(self._current_content)
        if title:
            self.sections.append((self._heading_level, title, content))
        self._current_content = []
        self._current_heading = []

    def handle_starttag(self, tag, attrs):
        if self._stopped:
            return
        if tag in self.SKIP_TAGS:
            self._skip += 1
            return
        if tag == "math":
            attrs_dict = dict(attrs)
            alttext = attrs_dict.get("alttext", "").strip()
            display  = attrs_dict.get("display", "inline")
            if alttext:
                fmt = f"$${alttext}$$" if display == "block" else f"${alttext}$"
                self._current_block.append(fmt)
            self._skip += 1
            return
        if tag in self.HEADING_TAGS:
            self._flush_block()
            self._flush_section()
            self._in_heading = True
            self._heading_level = int(tag[1])
            return
        if tag in self.BLOCK_TAGS:
            self._flush_block()

    def handle_endtag(self, tag):
        if tag in self.SKIP_TAGS or tag == "math":
            self._skip = max(0, self._skip - 1)
        if tag in self.HEADING_TAGS:
            self._in_heading = False

    def handle_data(self, data):
        if self._stopped or self._skip > 0:
            return
        stripped = data.strip()
        if not stripped:
            return
        if stripped.lower() in self.STOP_SECTIONS:
            self._flush_block()
            self._flush_section()
            self._stopped = True
            return
        if self._in_heading:
            self._current_heading.append(stripped)
        else:
            self._current_block.append(stripped)

    def get_sections(self):
        self._flush_block()
        self._flush_section()
        return self.sections


def _get_sections(arxiv_id):
    """Fetch paper HTML and parse into sections. Returns list or None."""
    arxiv_id = arxiv_id.replace("https://arxiv.org/abs/", "").replace("https://arxiv.org/pdf/", "")
    base_id  = arxiv_id.split("v")[0] if "v" in arxiv_id.split("/")[-1] else arxiv_id
    raw = _fetch_html(f"https://arxiv.org/html/{base_id}")
    if not raw or len(raw) < 2000:
        return None, "No HTML version available for this paper. Use: papers.py read " + arxiv_id
    parser = _SectionExtractor()
    parser.feed(raw)
    return parser.get_sections(), None


def toc(arxiv_id):
    """Show table of contents. HTML sections > PDF bookmarks > nothing."""
    sections, _ = _get_sections(arxiv_id)
    aid = arxiv_id.replace("https://arxiv.org/abs/", "").replace("https://arxiv.org/pdf/", "")
    base_id = aid.split("v")[0] if "v" in aid.split("/")[-1] else aid

    if sections:
        print(f"\nTable of Contents: {aid} (HTML)\n")
        for i, (level, title, content) in enumerate(sections):
            indent = "  " * (level - 1)
            words = len(content.split())
            print(f"  {indent}{i+1:>2}. {title}  ({words} words)")
        return

    # Try PDF bookmarks
    print(f"No HTML for {aid}. Trying PDF bookmarks...")
    pdf_bytes, pdf_err = _download_pdf_bytes(base_id)
    if not pdf_bytes:
        print(f"Could not download PDF: {pdf_err}")
        print(f"Use: uv run .agents/skills/research/scripts/papers.py read {aid}")
        return

    bm_toc, doc = _toc_from_pdf_bytes(pdf_bytes)
    if bm_toc:
        print(f"\nTable of Contents: {aid} (PDF bookmarks)\n")
        for level, title, page in bm_toc:
            indent = "  " * (level - 1)
            print(f"  {indent}p{page:>3}. {title}")
        print(f"\nUse: papers.py section {aid} <title keyword>")
    else:
        print("No bookmarks in PDF. Use full text:")
        print(f"  uv run .agents/skills/research/scripts/papers.py read {aid}")


def section(arxiv_id, query):
    """Extract a section. HTML sections > PDF bookmark page range > nothing."""
    aid = arxiv_id.replace("https://arxiv.org/abs/", "").replace("https://arxiv.org/pdf/", "")
    base_id = aid.split("v")[0] if "v" in aid.split("/")[-1] else aid

    # Try HTML first
    sections, _ = _get_sections(arxiv_id)
    if sections:
        matched_idx = None
        if query.isdigit():
            idx = int(query) - 1
            if 0 <= idx < len(sections):
                matched_idx = idx
        else:
            q = query.lower()
            for i, (_, title, _) in enumerate(sections):
                if q in title.lower():
                    matched_idx = i
                    break

        if matched_idx is None:
            print(f'Section not found: "{query}"')
            print("Run: papers.py toc  to see available sections.")
            return

        level, title, body = sections[matched_idx]
        parts = [body]
        for lvl, ttl, cnt in sections[matched_idx + 1:]:
            if lvl <= level:
                break
            parts.append(f"\n{'#' * lvl} {ttl}\n\n{cnt}")
        print(f"\n{'#' * level} {title}\n")
        print("\n".join(parts))
        return

    # Try PDF bookmarks
    pdf_bytes, _ = _download_pdf_bytes(base_id)
    if not pdf_bytes:
        print("No HTML and could not download PDF.")
        return

    bm_toc, doc = _toc_from_pdf_bytes(pdf_bytes)
    if not bm_toc or not doc:
        print(f"No HTML and no PDF bookmarks for {aid}.")
        print(f"Use: uv run .agents/skills/research/scripts/papers.py read {aid}")
        return

    q = query.lower()
    matched = None
    for i, (level, title, page) in enumerate(bm_toc):
        if q in title.lower():
            matched = i
            break

    if matched is None:
        print(f'Section not found: "{query}"')
        print("Run: papers.py toc  to see available sections.")
        return

    level, title, start_page = bm_toc[matched]
    end_page = doc.page_count + 1
    for lvl, ttl, pg in bm_toc[matched + 1:]:
        if lvl <= level:
            end_page = pg
            break

    pages = [doc[i].get_text() for i in range(start_page - 1, min(end_page - 1, doc.page_count))]
    text = "\n\n".join(p for p in pages if p.strip())
    print(f"\n## {title} (p{start_page}-{end_page-1})\n")
    print(text)


def related(arxiv_id, limit=10):
    """Find related papers via Semantic Scholar."""
    arxiv_id = arxiv_id.replace("https://arxiv.org/abs/", "").replace("https://arxiv.org/pdf/", "")
    sch = get_s2()
    papers = safe_s2_call(sch.get_recommended_papers, f"ArXiv:{arxiv_id}", limit=limit, fields=[
        "title", "authors", "year", "abstract", "url", "citationCount", "externalIds"
    ])
    if not papers:
        print("No related papers found.")
        return
    for i, p in enumerate(papers):
        aid = (p.externalIds or {}).get("ArXiv", "")
        authors = [a.name for a in (p.authors or [])]
        print(f"\n[{i+1}] {aid}")
        print(fmt_paper(p.title or "Untitled", authors, p.year or "?",
                        p.abstract, p.url or "", citations=p.citationCount))


def citations(arxiv_id, limit=20):
    """Papers citing this one — forward snowball."""
    arxiv_id = arxiv_id.replace("https://arxiv.org/abs/", "").replace("https://arxiv.org/pdf/", "")
    sch = get_s2()
    paper = safe_s2_call(sch.get_paper, f"ArXiv:{arxiv_id}", fields=[
        "title", "citations.title", "citations.authors", "citations.year",
        "citations.url", "citations.citationCount", "citations.externalIds"
    ])
    if not paper or not paper.citations:
        print("No citations found.")
        return
    cits = sorted(paper.citations, key=lambda p: p.citationCount or 0, reverse=True)[:limit]
    print(f"\nPapers citing: {paper.title}\n")
    for i, p in enumerate(cits):
        aid = (p.externalIds or {}).get("ArXiv", "")
        authors = [a.name for a in (p.authors or [])]
        print(f"[{i+1}] {aid}  ({p.citationCount or 0} cites)")
        print(f"  {p.title}")
        print(f"  {', '.join(authors[:3])}{'...' if len(authors) > 3 else ''} ({p.year or '?'})")
        print(f"  {p.url or ''}\n")


def references(arxiv_id, limit=20):
    """Papers cited by this one — backward snowball."""
    arxiv_id = arxiv_id.replace("https://arxiv.org/abs/", "").replace("https://arxiv.org/pdf/", "")
    sch = get_s2()
    paper = safe_s2_call(sch.get_paper, f"ArXiv:{arxiv_id}", fields=[
        "title", "references.title", "references.authors", "references.year",
        "references.url", "references.citationCount", "references.externalIds"
    ])
    if not paper or not paper.references:
        print("No references found.")
        return
    refs = sorted(paper.references, key=lambda p: p.citationCount or 0, reverse=True)[:limit]
    print(f"\nPapers cited by: {paper.title}\n")
    for i, p in enumerate(refs):
        aid = (p.externalIds or {}).get("ArXiv", "")
        authors = [a.name for a in (p.authors or [])]
        print(f"[{i+1}] {aid}  ({p.citationCount or 0} cites)")
        print(f"  {p.title}")
        print(f"  {', '.join(authors[:3])}{'...' if len(authors) > 3 else ''} ({p.year or '?'})")
        print(f"  {p.url or ''}\n")


def index(literature_dir="literature", lint=False):
    """Generate or update literature/index.md from YAML frontmatter."""
    lit_path = Path(literature_dir)
    if not lit_path.exists():
        print(f"Directory not found: {literature_dir}")
        return

    index_path = lit_path / "index.md"
    papers = []
    warnings = []

    for f in sorted(lit_path.glob("*.md")):
        if f.name in ("index.md", "_survey.md"):
            continue

        text = f.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not match:
            warnings.append(f"  ⚠ no frontmatter: {f.name}")
            continue

        fm = {}
        for line in match.group(1).splitlines():
            if ":" in line:
                key, _, val = line.partition(":")
                fm[key.strip()] = val.strip().strip('"').strip("'")

        missing = [k for k in ["title", "year", "tags", "status"] if not fm.get(k)]
        if missing:
            warnings.append(f"  ⚠ missing {', '.join(missing)}: {f.name}")

        papers.append({
            "file": f.name,
            "title": fm.get("title", "Untitled")[:60],
            "year": fm.get("year", "?"),
            "contribution": fm.get("contribution", "—"),
            "tags": fm.get("tags", "").strip("[]"),
            "status": fm.get("status", "?"),
        })

    papers.sort(key=lambda p: str(p["year"]), reverse=True)

    lines = [
        "# Literature Index",
        f"*Updated: {date.today()} · {len(papers)} paper{'s' if len(papers) != 1 else ''}*",
        "",
        "| File | Title | Year | Contribution | Tags | Status |",
        "|------|-------|------|-------------|------|--------|",
    ]
    for p in papers:
        link = f"[{p['file']}]({p['file']})"
        lines.append(f"| {link} | {p['title']} | {p['year']} | {p['contribution']} | {p['tags']} | {p['status']} |")

    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Updated {index_path} ({len(papers)} papers)")

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(w)
    elif lint:
        print("\n✓ No issues found")


# ── CLI ───────────────────────────────────────────────────────────────────────

COMMANDS = {
    "search":     (search,     "search <query> [limit]",          "Search papers by topic"),
    "fetch":      (fetch,      "fetch <arxiv_id>",                 "Abstract + metadata only"),
    "read":       (read,       "read <arxiv_id>",                  "Full paper text (HTML → PDF)"),
    "toc":        (toc,        "toc <arxiv_id>",                   "Table of contents"),
    "section":    (section,    "section <arxiv_id> <name|number>", "Extract a specific section"),
    "bibtex":     (bibtex,     "bibtex <arxiv_id>",                "BibTeX citation"),
    "related":    (related,    "related <arxiv_id> [limit]",       "Related papers"),
    "citations":  (citations,  "citations <arxiv_id> [limit]",     "Papers citing this (forward snowball)"),
    "references": (references, "references <arxiv_id> [limit]",    "Papers cited by this (backward snowball)"),
    "index":      (index,      "index [literature/] [--lint]",     "Generate/update literature/index.md"),
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("Usage: papers.py <command> [args]\n")
        print("Commands:")
        for _, (_, usage, desc) in COMMANDS.items():
            print(f"  {usage:<45} {desc}")
        print("\nRequires: pip install arxiv semanticscholar pdfplumber")
        print("Optional: SEMANTIC_SCHOLAR_API_KEY env var for higher rate limits")
        sys.exit(1)

    cmd = sys.argv[1]
    func = COMMANDS[cmd][0]
    args = sys.argv[2:]

    if cmd == "search":
        query = " ".join(args[:-1]) if args and args[-1].isdigit() else " ".join(args)
        limit = int(args[-1]) if args and args[-1].isdigit() else 10
        func(query, limit)
    elif cmd == "section":
        if len(args) < 2:
            sys.exit("Usage: papers.py section <arxiv_id> <name|number>")
        func(args[0], " ".join(args[1:]))
    elif cmd == "index":
        lit_dir = next((a for a in args if not a.startswith("--")), "literature")
        lint = "--lint" in args
        func(lit_dir, lint)
    elif cmd in ("related", "citations", "references"):
        if not args:
            sys.exit(f"Usage: papers.py {cmd} <arxiv_id> [limit]")
        limit = int(args[1]) if len(args) > 1 else (10 if cmd == "related" else 20)
        func(args[0], limit)
    else:
        if not args:
            sys.exit(f"Usage: papers.py {cmd} <arxiv_id>")
        func(args[0])


if __name__ == "__main__":
    main()
