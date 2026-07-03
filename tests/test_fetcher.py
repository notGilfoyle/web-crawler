import pytest

from app.fetcher import Fetcher


@pytest.mark.anyio
async def test_fetch_example():
    fetcher = Fetcher()

    html = await fetcher.fetch("https://example.com")

    assert html is not None
    assert "<html" in html.lower()