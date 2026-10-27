# Satellite Imagery Metadata Aggregator API

A FastAPI backend project demonstrating asynchronous Python
programming and concurrent satellite metadata retrieval.

## Tech Stack

- Python 3.11+
- FastAPI
- asyncio
- HTTPX (planned integration)
- Pydantic
- pytest

## Features

- Asynchronous REST API endpoints
- Concurrent satellite metadata retrieval
- Simulated Sentinel-1, Sentinel-2, and Landsat-9 services
- Execution time measurement

## Local Setup

Create a virtual environment:

    py -m venv .venv

Activate it on Windows:

    .venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

Start the API:

    python -m uvicorn app.main:app --reload

Open Swagger UI:

    http://127.0.0.1:8000/docs

## API Endpoints

GET /

GET /satellites/metadata

## Roadmap

- Integrate real external HTTP APIs
- Add request timeouts and error handling
- Implement concurrency limits
- Add automated tests and logging
