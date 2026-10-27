import asyncio
import time
from fastapi import FastAPI

app = FastAPI(title = "Satellite Metadata API")

async def fetch_satellite_metadata(name:str, delay:float):
  print(f"Starting fetch: {name}")

  await asyncio.sleep(delay)

  print(f"Completed fetch: {name}")

  return{
    "satellite": name,
    "status": "available",
    "processing_time": delay
  }

@app.get("/")
async def root():
  return {"message": "Satellite Metadata API is running"}

@app.get("/satellites/metadata")
async def get_satellite_metadata():
  start = time.perf_counter()

  results = await asyncio.gather(
    fetch_satellite_metadata("Sentinel-1", 3),
    fetch_satellite_metadata("Sentinel-2", 2),
    fetch_satellite_metadata("Landsat-9", 1),
    fetch_satellite_metadata("TerraSAR-X", 4),
  )

  elapsed = time.perf_counter() - start

  return {
    "satellites": results,
    "total_time": round(elapsed, 2)
  }