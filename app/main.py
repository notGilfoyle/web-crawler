from fastapi import FastAPI

app = FastAPI(
    title="Simple Web Crawler",
    version="1.0.0",
    description="A simple asynchronous web crawler built with FastAPI."
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Simple Web Crawler!"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }