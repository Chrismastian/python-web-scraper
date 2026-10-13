"""Ambil HTML dari internet."""
import requests


def fetch(url):
    """Ambil HTML dari url, balikin string HTML-nya."""
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.text
