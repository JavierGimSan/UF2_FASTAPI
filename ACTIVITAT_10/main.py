from fastapi import FastAPI
from typing import List
import paraules_sch
from metodes_queries import read_tematiques

app = FastAPI()

@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def get_tematiques():
    return paraules_sch.tematiques_schema(read_tematiques())