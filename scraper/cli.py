import argparse

from scraper import fetch, parse


def main() -> None:
    parser = argparse.ArgumentParser(description="Scraper kutipan sederhana")
    parser.add_argument("url", help="URL halaman kutipan (contoh: https://quotes.toscrape.com/)")
    args = parser.parse_args()

    html = fetch.fetch(args.url)
    quotes = parse.parse_quotes(html)

    if not quotes:
        print("(tidak ada kutipan)")
        return
    for i, q in enumerate(quotes, 1):
        tags = ", ".join(q["tags"]) if q["tags"] else "-"
        print(f'{i}. "{q["text"]}"')
        print(f"   - {q['author']}  [{tags}]")


if __name__ == "__main__":
    main()
