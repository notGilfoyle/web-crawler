from app.utils import normalize_url


def test_relative_url():

    assert normalize_url(
        "https://example.com",
        "/about"
    ) == "https://example.com/about"


def test_remove_fragment():

    assert normalize_url(
        "https://example.com",
        "/about#team"
    ) == "https://example.com/about"


def test_ignore_mailto():

    assert normalize_url(
        "https://example.com",
        "mailto:test@example.com"
    ) is None


def test_ignore_javascript():

    assert normalize_url(
        "https://example.com",
        "javascript:void(0)"
    ) is None