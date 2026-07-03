from fastapi import FastAPI

from app.crawler import WebCrawler

app = FastAPI(
    title="Simple Web Crawler"
)

crawler = WebCrawler()


@app.get("/")
async def root():
    return {
        "message": "Simple Web Crawler"
    }


@app.get("/crawl")
async def crawl(
    url: str,
    depth: int = 2,
):

    pages = await crawler.crawl(
        url,
        max_depth=depth,
    )

    return {
        "pages": pages,
        "visited": len(crawler.visited),
    }