"""Parse HTML jadi data terstruktur.

Fungsi ini TERIMA STRING HTML (bukan URL) supaya bisa dites tanpa internet.
"""
from bs4 import BeautifulSoup


def parse_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    quotes = soup.select("div.quote")
    result = []
    for q in quotes:
     text   = q.select_one("span.text").get_text(strip=True)
     author = q.select_one("small.author").get_text(strip=True)
     tags   = [t.get_text(strip=True) for t in q.select("a.tag")]
     result.append({"text": text, "author": author, "tags": tags})
    return result
