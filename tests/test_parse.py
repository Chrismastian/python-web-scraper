from scraper import parse

# Sample HTML — tested WITHOUT the network (the key: parse takes a string, not a URL)
SAMPLE_HTML = """
<html><body>
  <div class="quote">
    <span class="text">"Hello world"</span>
    <small class="author">Alice</small>
    <div class="tags">
      <a class="tag">greeting</a>
      <a class="tag">start</a>
    </div>
  </div>
  <div class="quote">
    <span class="text">"Keep learning"</span>
    <small class="author">Bob</small>
    <div class="tags">
      <a class="tag">motivation</a>
    </div>
  </div>
</body></html>
"""


def test_parse_quotes_count():
    quotes = parse.parse_quotes(SAMPLE_HTML)
    assert len(quotes) == 2


def test_parse_quotes_fields():
    quotes = parse.parse_quotes(SAMPLE_HTML)
    assert quotes[0] == {"text": '"Hello world"', "author": "Alice", "tags": ["greeting", "start"]}
    assert quotes[1]["author"] == "Bob"
    assert quotes[1]["tags"] == ["motivation"]


def test_parse_empty():
    assert parse.parse_quotes("<html><body>empty</body></html>") == []
