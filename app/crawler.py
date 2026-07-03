import asyncio

from app.fetcher import Fetcher
from app.frontier import URLFrontier
from app.parser import Parser


class WebCrawler:

    def __init__(self):

        self.fetcher = Fetcher()
        self.parser = Parser()
        self.frontier = URLFrontier()

        self.visited = set()
        self.results = []

    async def crawl(self, seed_url: str, max_depth: int = 2):

        self.visited.clear()
        self.results.clear()
        self.frontier = URLFrontier()

        await self.frontier.add(seed_url, 0)

        while not self.frontier.empty():

            url, depth = await self.frontier.get()

            await self.process_page(
                url=url,
                depth=depth,
                max_depth=max_depth,
            )

        return self.results

    async def process_page(
        self,
        url: str,
        depth: int,
        max_depth: int,
    ):

        if url in self.visited:
            return

        self.visited.add(url)

        print(f"[Depth {depth}] {url}")

        html = await self.fetcher.fetch(url)

        if html is None:
            return

        page = self.parser.parse(html, url)

        self.results.append(
            {
                "url": url,
                "title": page["title"],
                "depth": depth,
            }
        )

        if depth >= max_depth:
            return

        for link in page["links"]:

            if link not in self.visited:

                await self.frontier.add(
                    link,
                    depth + 1,
                )