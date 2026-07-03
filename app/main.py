from fastapi import FastAPI
from app.fetcher import Fetcher

app = FastAPI(
    title="Simple Web Crawler",
    version="1.0.0",
)

fetcher = Fetcher()


@app.get("/")
async def root():
    return {
        "message": "Simple Web Crawler"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@app.get("/fetch")
async def fetch(url: str):
    """
    Example:
    /fetch?url=https://example.com
    """
    html = await fetcher.fetch(url)

    if html is None:
        return {
            "success": False
        }

    return {
        "success": True,
        "length": len(html)
    }