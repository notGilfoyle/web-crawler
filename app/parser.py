from bs4 import BeautifulSoup

from app.utils import normalize_url


class Parser:

    def parse(self, html: str, base_url: str) -> dict:

        soup = BeautifulSoup(html, "html.parser")

        title = ""

        if soup.title and soup.title.string:
            title = soup.title.string.strip()

        links = set()

        for anchor in soup.find_all("a", href=True):

            url = normalize_url(base_url, anchor["href"])

            if url:
                links.add(url)

        return {
            "title": title,
            "links": sorted(links)
        }