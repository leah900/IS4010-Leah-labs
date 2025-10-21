
# AGENTS.md

## Project Overview
This project is a Chuck Norris Joke CLI tool that fetches jokes from the public Chuck Norris API. It demonstrates AI-assisted development, including planning, coding, testing, and documentation.

## API Used
- Chuck Norris Jokes API: https://api.chucknorris.io/
- Endpoints: /jokes/random, /jokes/categories, /jokes/search

## CLI Commands
- `random`: Get a random Chuck Norris joke
- `categories`: List all available joke categories
- `search <query>`: Search for jokes containing a keyword

## Code Organization
- `src/main.py`: CLI entry point using argparse
- `src/api.py`: API interaction functions
- `tests/`: Test suite with mocking

## Technology Stack
- Python 3.10+
- argparse
- requests
- pytest
- unittest.mock
- GitHub Actions for CI/CD

## Coding Standards
- PEP 8 style
- Docstrings for all functions
- Error handling for API/network issues
- Mocking for all API calls in tests

## AI Assistance
- Used GitHub Copilot for code suggestions and test generation
- Used Copilot Chat for architecture and documentation guidance
- Used AI to scaffold project structure and write README
- GitHub Copilot (optional): inline completions while authoring.

## Style and constraints
- Python 3.10+ recommended.
- Use `requests` for HTTP.
- Ensure no real network calls in tests; always mock `requests.get`.
- Docstrings for all public functions.
```
