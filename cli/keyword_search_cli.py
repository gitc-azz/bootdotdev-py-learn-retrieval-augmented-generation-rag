import argparse

# from bootdotdev-py-learn-retrieval-augmented-generation-rag.search.exact_search import search as basic_search
from exact_search import search as basic_search


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")
            findings = basic_search("./data/movies.json", args.query)
            for found in findings:
                print(found)
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
