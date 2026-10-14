import argparse

from scraper import fetch, parse


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple quote scraper")
    parser.add_argument("url", help="Quote page URL (e.g. https://quotes.toscrape.com/)")
    args = parser.parse_args()

    html = fetch.fetch(args.url)
    quotes = parse.parse_quotes(html)

    if not quotes:
        print("(no quotes found)")
        return
    for i, q in enumerate(quotes, 1):
        tags = ", ".join(q["tags"]) if q["tags"] else "-"
        print(f'{i}. "{q["text"]}"')
        print(f"   - {q['author']}  [{tags}]")


if __name__ == "__main__":
    main()
