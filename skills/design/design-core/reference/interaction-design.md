# Interaction Design

## Progressive disclosure

Show the minimum needed to start. Reveal complexity only when the user asks for it — advanced options behind expandable sections, secondary actions visible only on hover, detail revealed on click. This reduces cognitive load without hiding capability.

The opposite (dumping everything at once) forces users to filter noise before they can act.

## Optimistic UI

Update the interface immediately on user action, sync with the server in the background, roll back on failure. Users perceive the app as faster because the action feels instant. Only block the UI when the operation genuinely can't be undone.

## Forms

- One question at a time where possible. Multi-step reduces drop-off on long forms.
- Show format expectations with an example, not just a label: "Date of birth (DD/MM/YYYY)" with a placeholder showing the format.
- Inline validation on blur (not on every keystroke — that's annoying). On submit for multi-step.
- Error messages: plain language + specific cause + how to fix. "Email is missing an @ symbol. Try: name@example.com" not "Invalid input".
- Never wipe form content on error. Preserve what the user typed.
- Destructive actions (delete, overwrite) need confirmation with specific language: "Delete 'Project Alpha'? This can't be undone." not "Are you sure?"

## Focus management

Keyboard users navigate entirely through focus. When a modal opens, move focus to it. When it closes, return focus to the trigger. When a form error appears, move focus to the first error. When a new page loads, focus the `<h1>` or main content.

Focus indicators must be visible. `outline: none` without a replacement is an accessibility failure that affects keyboard and switch users.

## Loading patterns

Match the pattern to the duration:
- < 300ms: no indicator (the result appears before the user notices)
- 300ms – 2s: spinner or button loading state
- 2s – 10s: progress bar with estimated time if possible
- > 10s: background processing with notification on completion

Skeleton screens (gray placeholder shapes) reduce perceived wait time for content-heavy loads because they set layout expectations before data arrives.

## Empty states

Empty states are the first thing many new users see. They should:
1. Explain why it's empty (first time? no results? filtered out?)
2. Show the primary action to fill it
3. Be visually friendly, not a dead end

"No projects yet. [Create your first project →]" beats "No items found."

## Error states

Errors are moments of user frustration. The message should:
- Use plain language (no error codes for end users)
- Say what happened, not just that something failed
- Give a specific next step
- Preserve any work the user did

Network errors should offer retry. Not-found errors should offer navigation. Permission errors should explain how to request access.
