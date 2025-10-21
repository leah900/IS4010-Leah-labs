# Chuck Norris Joke CLI

![Tests](https://github.com/leah900/IS4010-Leah-labs/workflows/Tests/badge.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Description
A command-line tool to fetch Chuck Norris jokes from the public API. Supports random jokes, listing categories, and searching jokes by keyword.

## Features
- Get a random Chuck Norris joke
- List all joke categories
- Search jokes by keyword

## Installation
```bash
# Clone the repository
https://github.com/leah900/IS4010-Leah-labs.git
cd IS4010-Leah-labs/chuck-norris-cli

# (Optional) Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
python -m src.main random
python -m src.main categories
python -m src.main search "infinity"
```

## API Information
- [Chuck Norris Jokes API](https://api.chucknorris.io/)

## Testing
```bash
pytest tests/
```

## Technologies
- Python 3.10+
- argparse
- requests
- pytest
- unittest.mock
- GitHub Actions

## License
MIT
