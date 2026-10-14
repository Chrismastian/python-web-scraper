"""Fetch HTML from the internet."""
import requests


def fetch(url):
    """Fetch HTML from url, return it as a string."""
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.text
