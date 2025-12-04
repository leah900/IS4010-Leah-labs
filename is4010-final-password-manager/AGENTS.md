# AI Agents and Prompts

## Tools used
- GitHub Copilot — in-editor completions and boilerplate
- ChatGPT/GPT-4 — design decisions, debugging, and test writing

## Example prompts
- "Show me how to encrypt/decrypt strings using cryptography.Fernet in Python"
- "Write pytest tests for a function that encrypts and decrypts data"

## Categorized example prompts

- Design & architecture
	- "Propose a minimal, secure on-disk format for an encrypted password store and outline safe IO patterns."
	- "How should I structure a small CLI Python package so tests can import the code easily in CI?"

- Security & crypto
	- "What are safe PBKDF2 parameters for deriving a symmetric key in 2025 for local storage?"
	- "Show how to use cryptography.hazmat.primitives.kdf.pbkdf2.PBKDF2HMAC correctly with Fernet."

- Testing & TDD
	- "Write pytest tests that create a temporary encrypted store, add entries, and then validate decryption with the master password."
	- "How can I test error handling when the store file is corrupted?"

- CLI UX & Help text
	- "Draft concise `click` command help strings for `init`, `add`, `get`, `list`, `update`, `delete`, and `search` commands."

## Prompts actually used (representative)
- "Create a Python package that implements a password store using PBKDF2 + Fernet, with functions to init/load/save/add/get/list/update/delete/search entries. Include tests using pytest and an example Click CLI." (Used to scaffold the initial project.)
- "Add a password generator function using `secrets` and `string` with options for length and use_symbols, and write tests for it." (Used to implement `generate_password`.)

## Review checklist applied to AI suggestions

- Verify cryptographic primitives and parameter choices (salt length, PBKDF2 iterations).
- Ensure secrets are generated with `secrets` module, not `random`.
- Validate that the CLI does not echo secrets to shell history by default.
- Keep test fixtures using `tempfile` and remove temporary files after tests.

## Attribution and human review

AI tools (GitHub Copilot, ChatGPT/GPT-4) were used to accelerate prototyping, create tests, and suggest implementations. All suggestions were reviewed and adjusted by the developer for correctness and security.


## Reflection
Using AI sped up boilerplate creation and helped craft tests. All AI-suggested code was reviewed and adapted to ensure security best practices.

## CI badge
The repository includes a GitHub Actions workflow for running the project's test suite; the README contains a status badge linked to that workflow.
