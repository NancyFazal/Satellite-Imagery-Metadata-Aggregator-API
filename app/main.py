import asyncio
import logging
import time
from turtle import delay
from fastapi import FastAPI

app = FastAPI(title = "Satellite Metadata API")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def fetch_satellite_metadata(name:str, delay:float):
  logger.info("Fetching metadata for %s", name)

  try:
    await asyncio.sleep(delay)

    if name == "Sentinel-2":
      raise RuntimeError("Simulated satellite service failure")

    return {
      "satellite": name,
      "status": "available",
      "metadata":{
        "product_type": "satellite_imagery"
      }
    }
  except asyncio.CancelledError:
    logger.warning("Request cancelled for %s", name)
    raise
  except Exception as exc:
    logger.error("Failed to fetch %s: %s", name, exc)

    return {
      "satellite": name,
      "status": "error",
      "error": str(exc)
    }
@app.get("/")
async def root():
  return {"message": "Satellite Metadata API is running"}

@app.get("/satellites/metadata")
async def get_satellite_metadata():
  start = time.perf_counter()

  satellites = [
    ("Sentinel-1", 3),
    ("Sentinel-2", 2),
    ("Landsat-9", 1)
  ]

  async with asyncio.TaskGroup() as group:
    tasks = [
      group.create_task(
        fetch_satellite_metadata(name, delay)
      )
      for name, delay in satellites
    ]
  results = [task.result() for task in tasks]

  elapsed = time.perf_counter() - start

  return {
    "satellites": results,
    "total_time": round(elapsed, 2)
  }