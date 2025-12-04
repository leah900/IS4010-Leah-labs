# AI-Assisted Development

Tools Used:
- GitHub Copilot
- ChatGPT

How AI Helped:
- Generated initial CLI boilerplate
- Suggested pytest tests
- Helped draft README and AGENTS.md content

Reflection:
AI helped speed iteration; all code was reviewed by the developer.

## Prompts used

- "Create a simple Python CLI to add/list/complete/delete tasks stored in a JSON file."
- "Write pytest tests that use tmp_path to avoid touching the repo state."

## Review checklist

- Validate that JSON read/write handles corrupted files gracefully (tests added).
- Ensure IDs increment correctly and duplicates are allowed for descriptions.
- Confirm no secrets or credentials are present in the repository.

## Notes

AI suggestions were adapted to match project constraints and to use standard library modules only.
