from scraper import parse

# HTML contoh — dites TANPA internet (ini kuncinya: parse terima string, bukan URL)
SAMPLE_HTML = """
<html><body>
  <div class="quote">
    <span class="text">"Halo dunia"</span>
    <small class="author">Budi</small>
    <div class="tags">
      <a class="tag">sapa</a>
      <a class="tag">awal</a>
    </div>
  </div>
  <div class="quote">
    <span class="text">"Belajar terus"</span>
    <small class="author">Ani</small>
    <div class="tags">
      <a class="tag">motivasi</a>
    </div>
  </div>
</body></html>
"""


def test_parse_quotes_count():
    quotes = parse.parse_quotes(SAMPLE_HTML)
    assert len(quotes) == 2


def test_parse_quotes_fields():
    quotes = parse.parse_quotes(SAMPLE_HTML)
    assert quotes[0] == {"text": '"Halo dunia"', "author": "Budi", "tags": ["sapa", "awal"]}
    assert quotes[1]["author"] == "Ani"
    assert quotes[1]["tags"] == ["motivasi"]


def test_parse_empty():
    assert parse.parse_quotes("<html><body>kosong</body></html>") == []
