import asyncio
from fastapi import FastAPI

from app.crawler import WebCrawler
from app.job_manager import JobManager

app = FastAPI(
    title="Simple Web Crawler"
)

crawler = WebCrawler()
jobs = JobManager()

@app.get("/")
async def root():
    return {
        "message": "Simple Web Crawler"
    }


@app.get("/crawl")
async def crawl(
    url: str,
    depth: int = 2,
    workers: int = 5,
):

    pages = await crawler.crawl(
        seed_url=url,
        max_depth=depth,
        workers=workers,
    )

    return {
        "visited": len(crawler.visited),
        "pages": pages,
    }