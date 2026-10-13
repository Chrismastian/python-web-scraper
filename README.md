# python-web-scraper

[![CI](https://github.com/Chrismastian/python-web-scraper/actions/workflows/ci.yml/badge.svg)](https://github.com/Chrismastian/python-web-scraper/actions/workflows/ci.yml)

Web scraper sederhana untuk belajar Python: ambil HTML dari internet, ubah jadi data terstruktur, lalu **bandingkan versi sync (`requests`) vs async (`httpx`)**.

Studi kasus: [quotes.toscrape.com](https://quotes.toscrape.com/) (situs latihan scraping).

## Cara pakai

Ambil 1 halaman (sync):

```bash
python -m scraper.cli https://quotes.toscrape.com/
```

Ambil 10 halaman sekaligus (async):

```bash
python -m scraper.async_fetch
```

## Sync vs async (kenapa async penting)

Mengambil 10 halaman berurutan (sync) memakan **~28 detik** — hampir semuanya waktu *menunggu server*, bukan kerja komputer.

Versi async mengambil 10 halaman **bersamaan**: **~5 detik** (≈6x lebih cepat).

| Versi | Cara | 10 halaman |
|-------|------|-----------|
| `scraper/fetch.py` | `requests`, satu per satu | ~28 detik |
| `scraper/async_fetch.py` | `httpx` + `asyncio.gather` | ~5 detik |

Poinnya: async **tidak** mempercepat server (server tetap lambat). Async mengisi waktu tunggu dengan permintaan lain.

## Development

```bash
pip install pytest requests beautifulsoup4 httpx
pytest
```

## Struktur

```
scraper/
  fetch.py        # ambil HTML (sync, requests)
  parse.py        # ubah HTML -> data (murni, tanpa internet)
  async_fetch.py  # ambil BANYAK halaman sekaligus (async, httpx)
  cli.py          # entry: url -> fetch -> parse -> cetak
tests/
  test_parse.py   # tes parse pakai HTML contoh (tanpa internet)
```

`parse.py` sengaja menerima **string HTML**, bukan URL — supaya bisa dites tanpa internet dan bisa dipakai oleh `fetch` (sync) maupun `async_fetch` (async) tanpa perubahan.
