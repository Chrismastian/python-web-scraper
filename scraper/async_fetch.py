"""Fetch MANY pages at once (async). Compare with the sync fetch.py."""
import asyncio
import time

import httpx


async def fetch_one(client, url):
    """Fetch one URL, return its HTML. Note the 'await' on client.get."""
    resp = await client.get(url)
    resp.raise_for_status()
    return resp.text


async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        tasks = [fetch_one(client, u) for u in urls]
        return await asyncio.gather(*tasks)


def main():
    urls = [f"https://quotes.toscrape.com/page/{i}/" for i in range(1, 11)]
    t = time.time()
    pages = asyncio.run(fetch_all(urls))
    print(f"{len(pages)} pages in {time.time() - t:.1f} seconds")


if __name__ == "__main__":
    main()
