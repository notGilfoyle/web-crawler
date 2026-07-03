from bs4 import BeautifulSoup
from urllib.parse import urljoin


class Parser:
    """
    Responsible for parsing HTML pages.
    """

    def parse(self, html: str, base_url: str) -> dict:
        """
        Returns:
        {
            "title": "...",
            "links": [...]
        }
        """

        soup = BeautifulSoup(html, "html.parser")

        title = ""

        if soup.title and soup.title.string:
            title = soup.title.string.strip()

        links = []

        for anchor in soup.find_all("a", href=True):
            href = anchor["href"]

            absolute_url = urljoin(base_url, href)

            links.append(absolute_url)

        return {
            "title": title,
            "links": links
        }