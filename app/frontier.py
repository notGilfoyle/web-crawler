import asyncio


class URLFrontier:
    """
    Queue of URLs waiting to be crawled.

    Each queue item is:
        (url, depth)
    """

    def __init__(self):
        self.queue = asyncio.Queue()

    async def add(self, url: str, depth: int):
        """
        Add a URL to the frontier.
        """
        await self.queue.put((url, depth))

    async def get(self):
        """
        Get the next URL.
        """
        return await self.queue.get()

    def empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()