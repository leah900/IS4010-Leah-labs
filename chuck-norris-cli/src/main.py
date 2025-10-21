
import argparse
from src.api import get_random_joke, get_categories, search_jokes

def main():
    parser = argparse.ArgumentParser(description="Chuck Norris Joke CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Random joke command
    parser_random = subparsers.add_parser("random", help="Get a random Chuck Norris joke")

    # Categories command
    parser_categories = subparsers.add_parser("categories", help="List all joke categories")

    # Search command
    parser_search = subparsers.add_parser("search", help="Search jokes by keyword")
    parser_search.add_argument("query", type=str, help="Keyword to search for in jokes")

    args = parser.parse_args()

    if args.command == "random":
        joke = get_random_joke()
        print(f"\n🤣 {joke}\n")
    elif args.command == "categories":
        categories = get_categories()
        print("Available categories:")
        for cat in categories:
            print(f"- {cat}")
    elif args.command == "search":
        jokes = search_jokes(args.query)
        if jokes:
            print(f"Jokes containing '{args.query}':")
            for joke in jokes:
                print(f"- {joke}")
        else:
            print(f"No jokes found containing '{args.query}'.")

if __name__ == "__main__":
    main()
