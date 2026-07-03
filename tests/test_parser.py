from app.parser import Parser


def test_parse_html():

    html = """
    <html>

        <head>
            <title>Example Page</title>
        </head>

        <body>

            <a href="/about">About</a>

            <a href="https://google.com">
                Google
            </a>

        </body>

    </html>
    """

    parser = Parser()

    result = parser.parse(
        html,
        "https://example.com"
    )

    assert result["title"] == "Example Page"

    assert "https://example.com/about" in result["links"]

    assert len(result["links"]) == 2

    assert result["links"] == sorted(result["links"])