import httpx

from app.config import DEFAULT_TIMEOUT, USER_AGENT


class Fetcher:

    def __init__(self):

        self.client = httpx.AsyncClient(
            timeout=DEFAULT_TIMEOUT,
            follow_redirects=True,
            headers={
                "User-Agent": USER_AGENT,
            },
        )

    async def fetch(self, url: str):

        try:

            response = await self.client.get(url)

            response.raise_for_status()

            return response.text

        except httpx.HTTPError as e:

            print(e)

            return None

    async def close(self):

        await self.client.aclose()