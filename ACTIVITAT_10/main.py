from fastapi import FastAPI
from typing import List
import paraules_sch
from metodes_queries import read_tematiques, read_all

app = FastAPI()

@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def get_tematiques():
    return paraules_sch.tematiques_schema(read_tematiques())

@app.get("/penjat/paraules/{tematica}", response_model=List[dict])
async def get_paraules_tematica(tematica: str):
    paraules = read_all(tematica)
    return paraules_sch.paraules_schema(paraules)