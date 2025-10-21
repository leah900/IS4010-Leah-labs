import unittest
from unittest.mock import patch
from src.main import main

class TestMain(unittest.TestCase):
    @patch("builtins.print")
    def test_main_run(self, mock_print):
        import sys
        sys.argv = ["main.py", "random"]
        main()

if __name__ == "__main__":
    unittest.main()


