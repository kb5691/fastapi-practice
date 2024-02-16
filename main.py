from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
  return {"message": "Hello World"}

@app.get("/countries/")
async def country(country_name: Optional[str] = None, country_number: Optional[int] = None):
  return {
    "country_name": country_name,
    "country_number": country_number
  }
