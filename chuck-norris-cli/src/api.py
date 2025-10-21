import requests


def get_random_joke():
    """Fetch a random Chuck Norris joke from the API."""
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["value"]
    except Exception:
        return "Oops! Couldn't fetch a joke right now."

def get_categories():
    """Fetch all available joke categories from the API."""
    url = "https://api.chucknorris.io/jokes/categories"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception:
        return []

def search_jokes(query):
    """Search for jokes containing the given keyword."""
    url = f"https://api.chucknorris.io/jokes/search?query={query}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [item["value"] for item in data.get("result", [])]
    except Exception:
        return []
