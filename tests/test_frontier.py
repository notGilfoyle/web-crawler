import pytest

from app.frontier import URLFrontier


@pytest.mark.anyio
async def test_queue():

    frontier = URLFrontier()

    await frontier.add("https://example.com", 0)

    assert frontier.size() == 1

    url, depth = await frontier.get()

    assert url == "https://example.com"

    assert depth == 0

    assert frontier.empty()