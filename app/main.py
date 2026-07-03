from fastapi import FastAPI
from app.frontier import URLFrontier


from app.fetcher import Fetcher
from app.parser import Parser

app = FastAPI()
frontier = URLFrontier()

fetcher = Fetcher()
parser = Parser()


@app.get("/")
async def root():
    return {
        "message": "Simple Web Crawler"
    }


@app.get("/parse")
async def parse(url: str):

    html = await fetcher.fetch(url)

    if html is None:
        return {
            "success": False
        }

    result = parser.parse(html, url)

    return result


@app.get("/frontier")
async def frontier_demo():

    await frontier.add("https://example.com", 0)

    url, depth = await frontier.get()

    return {
        "url": url,
        "depth": depth,
        "queue_size": frontier.size()
    }