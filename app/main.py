from fastapi import FastAPI

from app.fetcher import Fetcher
from app.parser import Parser

app = FastAPI()

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