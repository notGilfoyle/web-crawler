from app.fetcher import Fetcher
from app.frontier import URLFrontier
from app.parser import Parser


class WebCrawler:
    """
    Simple Breadth-First Web Crawler.
    """

    def __init__(self):
        self.fetcher = Fetcher()
        self.parser = Parser()
        self.frontier = URLFrontier()

        self.visited: set[str] = set()
        self.results: list[dict] = []

    async def crawl(self, seed_url: str, max_depth: int = 2):

        # Reset crawler state
        self.visited.clear()
        self.results.clear()
        self.frontier = URLFrontier()

        await self.frontier.add(seed_url, 0)

        while not self.frontier.empty():

            url, depth = await self.frontier.get()

            if url in self.visited:
                continue

            self.visited.add(url)

            print(f"Crawling: {url}")

            html = await self.fetcher.fetch(url)

            if html is None:
                continue

            page = self.parser.parse(html, url)

            self.results.append({
                "url": url,
                "title": page["title"],
                "depth": depth,
            })

            if depth >= max_depth:
                continue

            for link in page["links"]:

                if link not in self.visited:
                    await self.frontier.add(
                        link,
                        depth + 1,
                    )

        return self.results