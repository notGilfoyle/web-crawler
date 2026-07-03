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

        self.lock = asyncio.Lock()

    async def crawl(
        self,
        seed_url: str,
        max_depth: int = 2,
        workers: int = 5,
    ):

        self.visited.clear()
        self.results.clear()
        self.frontier = URLFrontier()

        await self.frontier.add(seed_url, 0)

        tasks = [
            asyncio.create_task(
                self.worker(max_depth)
            )
            for _ in range(workers)
        ]

        await self.frontier.queue.join()

        # Tell every worker to exit
        for _ in range(workers):
            await self.frontier.queue.put(None)

        await asyncio.gather(*tasks)

        return self.results

    async def worker(self, max_depth: int):

        while True:

            item = await self.frontier.queue.get()

            if item is None:
                self.frontier.queue.task_done()
                break

            url, depth = item

            try:
                await self.process_page(
                    url,
                    depth,
                    max_depth,
                )
            finally:
                self.frontier.queue.task_done()

    async def process_page(
        self,
        url: str,
        depth: int,
        max_depth: int,
    ):

        async with self.lock:

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

            async with self.lock:

                if link in self.visited:
                    continue

            await self.frontier.add(
                link,
                depth + 1,
            )