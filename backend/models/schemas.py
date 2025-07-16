from pydantic import BaseModel
from typing import List

class ClassifyRequest(BaseModel):
    message: str

class ClassifyResponse(BaseModel):
    category: str
    confidence: float

class Recommendation(BaseModel):
    location: str
    type: str
    score: float

class HeatmapCell(BaseModel):
    lat: float
    lon: float
    population: int
    service_count: int
    score: float 