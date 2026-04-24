# UX Writing

Interface text is the primary way users understand what to do. Bad copy creates confusion, support tickets, and abandonment. Good copy is invisible — users understand immediately without noticing the words.

---

## Principles

1. **Be specific**: "Save changes" not "Submit". "Email address" not "Enter value".
2. **Be concise**: cut unnecessary words, but not at the expense of clarity.
3. **Be active**: "We saved your changes" not "Changes have been saved".
4. **Be helpful**: tell users what to do, not just what happened.
5. **Be consistent**: same terms throughout. Don't alternate between "delete", "remove", and "trash" for the same action.
6. **Say it once**: no headers restating intros, no redundant explanations.

---

## Button and CTA labels

Describe the action specifically. Verb + noun.

| Instead of | Use |
|-----------|-----|
| Submit | Create account |
| OK | Got it |
| Click here | View pricing |
| Yes / No | Delete project / Keep project |
| Cancel (ambiguous) | Discard changes |

Primary action should be the most specific. Secondary action can be shorter.

---

## Error messages

Every error message needs three parts: what happened, why, and what to do next.

| Bad | Good |
|-----|------|
| Error 403 | You don't have permission to view this page. Contact your admin for access. |
| Invalid input | Email addresses need an @ symbol. Try: name@example.com |
| Something went wrong | We couldn't save your changes. Check your connection and try again. |
| Validation error | This field is required |

Don't blame the user. "You entered an invalid email" → "Email addresses need an @ symbol."

Place errors next to the field that caused them, not in a banner at the top of the page.

---

## Empty states

Empty states are often the first thing new users see. They should teach, not dead-end.

| Bad | Good |
|-----|------|
| No items | No projects yet. Create your first project to get started. → [Create project] |
| 0 results | No results for "xyz". Try a broader search or check spelling. |
| No messages | Inbox zero! You're all caught up. |

Structure: explain why it's empty + show the primary action to fill it + be encouraging, not clinical.

---

## Loading states

| Bad | Good |
|-----|------|
| Loading... (for 30 seconds) | Analyzing your data... this usually takes 30–60 seconds |
| (spinner, no text) | Saving changes... |
| Please wait | Almost there — syncing with your team's latest changes |

Explain what's happening when it's not obvious. Set time expectations when the operation is long.

Avoid cliché loading messages like "Herding pixels", "Teaching robots to dance", "Consulting the magic 8-ball" — these are recognizable AI-generated copy.

---

## Confirmation dialogs

State the specific action and its consequences. Use descriptive button labels.

| Bad | Good |
|-----|------|
| Are you sure? [Yes] [No] | Delete "Project Alpha"? This can't be undone. [Delete project] [Cancel] |
| Confirm action? [OK] [Cancel] | Publish this post? It will be visible to everyone. [Publish now] [Not yet] |

Only use confirmation dialogs for destructive or hard-to-reverse actions. Overusing them trains users to click through without reading.

---

## Form labels and hints

- Labels above or beside inputs — never use placeholder as the only label (it disappears when typing).
- Show format expectations with examples: "Phone number (e.g. +1 555-0123)" not "Enter phone".
- Explain why you're asking when it's not obvious: "Date of birth — used to verify your age".
- Keep hints before the field, not after.

---

## Success messages

| Bad | Good |
|-----|------|
| Success | Settings saved! Changes take effect immediately. |
| Done | Message sent to 3 recipients. |
| (nothing) | ✓ Copied to clipboard |

Confirm what happened. Mention what happens next if relevant. Be brief.

---

## Navigation labels

Be specific and descriptive. Match the user's mental model.

| Bad | Good |
|-----|------|
| Items | Your projects |
| Stuff | Team members |
| Settings (when there are 4 settings pages) | Account settings / Notification preferences / Billing |

Use language users understand — not internal jargon or database field names.
