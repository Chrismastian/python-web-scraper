"""Ambil BANYAK halaman sekaligus (async). Bandingkan dengan fetch.py yang sync."""
import asyncio
import time

import httpx


async def fetch_one(client, url):
    """Ambil 1 URL, balikin HTML-nya. Perhatikan 'await' di client.get."""
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
    print(f"{len(pages)} halaman dalam {time.time() - t:.1f} detik")


if __name__ == "__main__":
    main()
