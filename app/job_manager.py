import asyncio
import uuid


class JobManager:

    def __init__(self):

        self.jobs = {}

    def create_job(self):

        job_id = str(uuid.uuid4())

        self.jobs[job_id] = {
            "status": "running",
            "results": [],
            "visited": 0,
        }

        return job_id

    def update(self, job_id, crawler):

        self.jobs[job_id]["results"] = crawler.results

        self.jobs[job_id]["visited"] = len(crawler.visited)

    def complete(self, job_id):

        self.jobs[job_id]["status"] = "completed"

    def get(self, job_id):

        return self.jobs.get(job_id)