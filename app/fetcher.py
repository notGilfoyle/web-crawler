import httpx


class Fetcher:
    """
    Responsible for downloading HTML pages.
    """

    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    async def fetch(self, url: str) -> str | None:
        """
        Fetch the HTML content of a URL.

        Returns:
            HTML string if successful, otherwise None.
        """
        try:
            async with httpx.AsyncClient(
                follow_redirects=True,
                timeout=self.timeout,
            ) as client:

                response = await client.get(url)

                response.raise_for_status()

                return response.text

        except httpx.HTTPStatusError as e:
            print(f"HTTP Error ({e.response.status_code}): {url}")

        except httpx.RequestError as e:
            print(f"Request Error: {url} ({e})")

        except Exception as e:
            print(f"Unexpected Error: {e}")

        return None