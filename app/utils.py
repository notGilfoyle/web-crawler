from urllib.parse import urljoin, urlparse, urldefrag


def normalize_url(base_url: str, href: str) -> str | None:
    """
    Normalize a URL.

    Steps:
    1. Convert relative URLs to absolute.
    2. Remove URL fragments (#section).
    3. Ignore non-http(s) links.
    """

    if not href:
        return None

    # Convert relative -> absolute
    url = urljoin(base_url, href)

    # Remove #fragment
    url, _ = urldefrag(url)

    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        return None

    return url