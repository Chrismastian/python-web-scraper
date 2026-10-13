# python-web-scraper

[![CI](https://github.com/Chrismastian/python-web-scraper/actions/workflows/ci.yml/badge.svg)](https://github.com/Chrismastian/python-web-scraper/actions/workflows/ci.yml)

A simple web scraper built while learning Python: fetch HTML from the internet, turn it into structured data, and **compare a sync (`requests`) version against an async (`httpx`) one**.

Case study: [quotes.toscrape.com](https://quotes.toscrape.com/) (a scraping practice site).

## Usage

Fetch a single page (sync):

```bash
python -m scraper.cli https://quotes.toscrape.com/
```

Fetch 10 pages at once (async):

```bash
python -m scraper.async_fetch
```

## Sync vs async (why async matters)

Fetching 10 pages one by one (sync) takes **~28 seconds** — almost all of it spent *waiting on the server*, not doing work.

The async version fetches all 10 pages **concurrently**: **~5 seconds** (≈6x faster).

| Version | Approach | 10 pages |
|---------|----------|----------|
| `scraper/fetch.py` | `requests`, one at a time | ~28s |
| `scraper/async_fetch.py` | `httpx` + `asyncio.gather` | ~5s |

The point: async does **not** make the server faster (the server stays slow). Async fills the waiting time with other requests.

## Development

```bash
pip install pytest requests beautifulsoup4 httpx
pytest
```

## Structure

```
scraper/
  fetch.py        # fetch HTML (sync, requests)
  parse.py        # turn HTML -> data (pure, no network)
  async_fetch.py  # fetch MANY pages at once (async, httpx)
  cli.py          # entry point: url -> fetch -> parse -> print
tests/
  test_parse.py   # parse tests using sample HTML (no network)
```

`parse.py` deliberately accepts an **HTML string**, not a URL — so it can be tested without the network and reused by both `fetch` (sync) and `async_fetch` (async) unchanged.
