# Simple Web Crawler

A lightweight asynchronous web crawler built with Python and FastAPI.

## Features

- Async HTTP requests
- Breadth-First Search (BFS)
- URL deduplication
- Concurrent workers
- REST API
- Configurable crawl depth

## Tech Stack

- Python
- FastAPI
- httpx
- BeautifulSoup

## Run

```bash
pip install -r requirements.txt

uvicorn app.main:app --reload
```

Open

http://127.0.0.1:8000/docs