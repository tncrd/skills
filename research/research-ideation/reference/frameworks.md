# Ideation Frameworks

Ten complementary frameworks for discovering research ideas. Each targets a different cognitive mode. Use the routing table in SKILL.md to pick the right one, or browse several when exploring broadly.

Adapted from [Orchestra Research's brainstorming and creative thinking skills](https://github.com/Orchestra-Research/AI-research-SKILLs) (MIT).

---

## 1. Problem-First vs Solution-First

Research ideas originate from two modes. Knowing which you're in prevents building solutions without problems, or chasing problems without feasible approaches.

**Problem-First** (pain point → method): start with a concrete failure or bottleneck. Naturally impactful because the motivation is real. Risk: converges on incremental fixes.

**Solution-First** (new capability → application): start with a new tool or insight seeking application. Often drives breakthroughs. Risk: hammer looking for a nail.

**Workflow**:
1. Write your idea in one sentence
2. Classify: problem-first or solution-first?
3. If problem-first → verify the problem matters (who suffers? how much?)
4. If solution-first → identify at least two genuine problems it addresses
5. Articulate the gap: what cannot be done today that this enables?

---

## 2. Abstraction Ladder

Every research problem sits at a level of abstraction. Moving up, down, or sideways reveals ideas invisible at your current level.

| Direction | Action | Produces |
|-----------|--------|----------|
| **Up** (generalize) | Turn a result into a broader principle | Framework papers, theoretical contributions |
| **Down** (instantiate) | Test under extreme constraints | Empirical papers, failure analyses |
| **Sideways** (analogize) | Apply same level to adjacent domain | Transfer papers, cross-pollination |

**Workflow**:
1. State your current focus in one sentence
2. Move UP: what's the general principle? What class of problems?
3. Move DOWN: what's the most constrained instance? What happens at the extreme?
4. Move SIDEWAYS: where else does this pattern appear?
5. For each: is this a publishable contribution on its own?

**Example**:
- Current: "Improving retrieval accuracy for RAG systems"
- Up: "What makes context selection effective for any augmented generation?"
- Down: "How does retrieval degrade under adversarial document perturbation?"
- Sideways: "Database query optimization uses similar relevance ranking — what can we borrow?"

---

## 3. Tension and Contradiction Hunting

Breakthroughs often come from resolving tensions between goals everyone accepts as trade-offs. The question: is the trade-off fundamental, or an artifact of current methods?

**Common ML tensions**:

| Tension | Research opportunity |
|---------|-------------------|
| Performance ↔ Efficiency | Match SOTA with 10× less compute? |
| Privacy ↔ Utility | Federated/encrypted methods closing the accuracy gap? |
| Generality ↔ Specialization | When does fine-tuning beat prompting, and why? |
| Safety ↔ Capability | Alignment that improves rather than taxes capability? |
| Interpretability ↔ Performance | Mechanistic insights enabling better architectures? |
| Scale ↔ Accessibility | Small models replicating emergent behaviors? |

**Workflow**:
1. Pick your area
2. List the top 3–5 desiderata
3. Identify pairs treated as trade-offs
4. For each: fundamental or artifact?
5. If artifact → the reconciliation IS your contribution
6. If fundamental → characterizing the Pareto frontier is itself valuable

---

## 4. Bisociation (Combinatorial Creativity)

Connecting two previously unrelated frames of reference. Not analogy (similar things) — bisociation (surprising connections between different things).

**Systematic workflow**:
1. Pick two domains you know at least superficially
2. List 5–10 core primitives per domain
3. Cross-product: for each pair, ask "what would it mean to apply A's concept to B's problem?"
4. Filter: which combinations produce a non-trivial, testable question?
5. Validate: is the connection structural (mechanisms map) or just verbal (labels map)?

**Quality test**: a strong bisociation isn't "the network is like a brain" (surface metaphor) but "attention implements selective gating analogous to cognitive attention filtering" (structural mapping where the mechanism transfers).

---

## 5. Cross-Pollination (Analogy Transfer)

Borrowing structural ideas from other fields. Many foundational techniques emerged this way: attention from cognitive science, genetic algorithms from biology, adversarial training from game theory.

**Requirements for a valid analogy**:
- The source domain has a well-understood mechanism
- The target domain has a similar structural challenge
- The mapping is between mechanisms, not just surface features
- The transfer generates testable predictions

**Sources to mine**: biology, physics, economics, cognitive science, control theory, information theory, game theory. Read survey papers in adjacent fields — their "open problems" section may describe your next project.

---

## 6. Problem Reformulation

Breakthroughs often come not from solving the problem as stated, but from re-representing it.

| Strategy | Example |
|----------|---------|
| Change the objective | "Make it faster" → "Eliminate the computation entirely" |
| Change the representation | "Classify tokens" → "Generate the classification as text" |
| Change the scale | "Work on ImageNet" → "What happens on 100 examples?" |
| Change the constraint | "Fixed compute budget" → "What if compute were free?" |
| Invert the problem | "How to make models robust" → "How exactly do they fail?" |

**Workflow**: state your problem 5 different ways. Each reformulation may suggest a different approach. The reformulation that makes the problem easiest is usually the right one.

---

## 7. Inversion

Instead of asking "how to achieve X", ask "how to guarantee NOT-X" or "what would make X impossible?" Then avoid those conditions.

**Examples**:
- "How to train robust models" → "What training procedures guarantee brittleness?"
- "How to write a good paper" → "What guarantees a rejection?" (weak baselines, no ablations, overclaimed results)
- "How to scale efficiently" → "What creates scaling bottlenecks?"

Inversion often reveals the critical variables faster than direct optimization because failure modes are more concrete than success criteria.

---

## 8. Constraint Manipulation

Creativity thrives under constraints — but the RIGHT constraints. Deliberately adding or removing constraints generates ideas.

**Add constraints**:
- "Solve X with no gradient computation"
- "Solve X with a model that fits on a phone"
- "Solve X with only 100 labeled examples"

**Remove constraints**:
- "What if we had infinite compute?"
- "What if we had perfect labels?"
- "What if latency didn't matter?"

The added constraint forces creative solutions. The removed constraint reveals what's actually hard vs what's artificially hard.

---

## 9. Boundary Exploration

Push the known limits of a method to find where it breaks. The boundary between "works" and "doesn't work" is where the interesting research lives.

**Dimensions to push**:
- Scale (up and down): does it work on 10× more data? 10× less?
- Distribution: does it work on out-of-distribution data?
- Time: does it degrade over time? Under distribution shift?
- Composition: does it compose with other methods?
- Adversarial: can you break it intentionally?

**The finding**: "Method X works up to scale Y but fails beyond" is a publishable result if you can explain WHY.

---

## 10. Gap Mining

Systematically find what's NOT been done in a field.

**Where to find gaps**:
- "Future work" sections of recent papers
- Workshop papers (preliminary ideas not yet fully explored)
- Rejected paper reviews (if accessible) — reviewers identify weaknesses
- Comparison tables with empty cells (combinations not yet tried)
- Highly cited papers with no follow-up on specific claims

**Validation**: a gap exists for three possible reasons:
1. Nobody thought of it (rare but valuable)
2. Someone tried and it didn't work (check negative results, workshop papers)
3. The data/compute doesn't exist to test it (may be solvable now)

Check all three before committing. Reason 1 is gold. Reason 2 needs a new approach. Reason 3 needs a feasibility check.

---

## 11. Adjacent Possible (Kauffman)

Innovation happens at the boundary of what is currently reachable. New ideas become feasible once their prerequisites exist — which explains why simultaneous independent discovery is common. Multiple people reach the same boundary at the same time.

**Practical implication**: map what has recently become possible, then explore the space those enablers open.

**Workflow**:
1. List recent enablers (last 12–18 months): new hardware, new datasets, new open-source models, new theoretical results
2. For each enabler: "what was previously impossible or impractical that this now permits?"
3. Combine enablers: the most powerful opportunities arise at the intersection of multiple new enablers
4. Check timing: if your idea requires technology that doesn't exist yet → park it. If it could have been done 5 years ago → someone probably tried it

**Timing signal**: ideas that became feasible in the last 6–18 months are in the sweet spot — technically possible, but not yet crowded.

---

## 12. Janusian / Dialectical Thinking

Holding two contradictory ideas simultaneously — not to choose between them, but to generate a synthesis that transcends the opposition. Named after Janus (two-faced Roman god). Different from Tension Hunting (which identifies trade-offs): this actively seeks a new framework that makes both goals achievable.

**In ML research, the most influential results often resolve apparent contradictions**:

| Contradiction | Resolution | Impact |
|--------------|------------|--------|
| Memorization ↔ Generalization | Grokking: models memorize first, then generalize | New understanding of learning dynamics |
| Safety ↔ Capability | Constitutional AI: alignment as a training signal, not a constraint | New RLHF paradigm |
| Expressiveness ↔ Efficiency | Sparse MoE: activate only relevant experts | Scalable architecture |
| Scale ↔ Accessibility | Distillation: transfer capability to smaller models | Open-source ecosystem |

**Workflow**:
1. Identify a binary in your field: A vs B (two approaches treated as opposites)
2. Resist choosing a side. Ask: "what would a system that achieves both look like?"
3. Ask: "is this trade-off fundamental, or an artifact of how the problem is formalized?"
4. Seek synthesis: the resolution often requires a new abstraction that reframes the relationship
5. Test: does the synthesis generate new predictions, or is it just a compromise?

---

## Running an ideation session

Frameworks work best in combination. A structured session:

### Phase 1: Diverge (generate candidates, no filtering)
1. **Tension Hunting** — list 3–5 trade-offs in your field
2. **Adjacent Possible** — list what became feasible in the last 12–18 months
3. **Boundary Exploration** — pick 2 popular methods and find where they break
4. **Bisociation** — cross-product with one idea from an adjacent field
5. **Abstraction Ladder** — for each candidate, generate up/down/sideways variants

Target: 10–20 raw ideas. Don't evaluate yet.

### Phase 2: Converge (filter to 3–5)

| Filter | Question | Drop if... |
|--------|----------|------------|
| Problem-first check | Is the problem genuine and important? | No one suffers from this |
| Two-sentence test | Can you state it in two sentences? | You can't yet |
| Feasibility | Can you start this week? | Clearly infeasible |
| Novelty | Has this been tried? | Check reason 2 in Gap Mining |

**Two-sentence test**: *"[Domain] currently struggles with [problem] because [reason]. We propose [approach], which works because [mechanism]."* If you can't complete both sentences, the idea isn't ready.

### Phase 3: Refine (sharpen the winner)
1. Identify the core tension being resolved
2. List 3 concrete experiments that would validate it
3. Define the minimum viable experiment (target: < 2 weeks)
4. State the strongest objection and your response

---

## Common blocks and fixes

| Block | Symptom | Framework |
|-------|---------|----------|
| Fixation | Can't stop seeing the problem one way | Reformulation |
| Tunnel vision | All ideas from the same subfield | Bisociation or Cross-Pollination |
| Incrementalism | Every idea is "+2% on benchmark" | Constraint Manipulation or Abstraction Ladder |
| Analysis paralysis | Too many options, can't commit | Adjacent Possible — what's feasible *now*? |
| False dichotomy | Stuck choosing between two approaches | Janusian Thinking |
| Wrong timing | "This is too hard" | Adjacent Possible — has something changed? |

## Common pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Novelty without impact | "No one has done X" but no one needs X | Problem-first check |
| Complexity worship | Method has 8 components, each marginal | Constraint Manipulation: simplify the rules |
| Echo chamber | All ideas from the same 10 papers | Bisociation: import from another field |
| Stale assumptions | "This was tried and didn't work" (5 years ago) | Adjacent Possible: what changed since? |
| Premature convergence | Committed to first idea without exploring | Run the full Diverge phase first |
