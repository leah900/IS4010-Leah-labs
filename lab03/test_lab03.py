name: run-pytest

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        python-version: ["3.10"]
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest
      
      - name: Test with pytest
        run: |
          pytest lab03/

lab01		lab02		lab03		test_lab03.py
liyatslassie@MacBookPro IS4010-Leah-labs % mkdir -p .github/workflows
nano .github/workflows/main.yml
nano lab03/test_lab03.py


  UW PICO 5.09                File: .github/workflows/main.yml                  


lab01		lab02		lab03		test_lab03.py
liyatslassie@MacBookPro IS4010-Leah-labs % mkdir -p .github/workflows
nano .github/workflows/main.yml
nano lab03/test_lab03.py


  UW PICO 5.09                File: .github/workflows/main.yml                  


≠øø=
