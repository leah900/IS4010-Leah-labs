import unittest
from unittest.mock import patch, MagicMock
from src.api import get_random_joke, get_categories, search_jokes

class TestAPI(unittest.TestCase):
    def test_get_random_joke(self):
        """Test that get_random_joke returns a non-empty string."""
        joke = get_random_joke()
        self.assertIsInstance(joke, str)          # Check it's a string
        self.assertGreater(len(joke), 0)          # Check it's not empty

    @patch('src.api.requests.get')
    def test_get_categories_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = ["animal", "career", "celebrity"]
        mock_get.return_value = mock_response
        self.assertEqual(get_categories(), ["animal", "career", "celebrity"])

    @patch('src.api.requests.get')
    def test_get_categories_failure(self, mock_get):
        mock_get.side_effect = Exception("API error")
        self.assertEqual(get_categories(), [])

    @patch('src.api.requests.get')
    def test_search_jokes_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": [
                {"value": "Chuck Norris counted to infinity. Twice."},
                {"value": "Chuck Norris can slam a revolving door."}
            ]
        }
        mock_get.return_value = mock_response
        jokes = search_jokes("Chuck")
        self.assertEqual(jokes, [
            "Chuck Norris counted to infinity. Twice.",
            "Chuck Norris can slam a revolving door."
        ])

    @patch('src.api.requests.get')
    def test_search_jokes_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        jokes = search_jokes("Chuck")
        self.assertEqual(jokes, [])

if __name__ == "__main__":
    unittest.main()

