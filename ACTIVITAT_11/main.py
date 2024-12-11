from fastapi import FastAPI
from typing import List
import paraules_sch
from metodes_queries import read_tematiques, read_all, read_lletres_idioma

app = FastAPI()

@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def get_tematiques():
    return paraules_sch.tematiques_schema(read_tematiques())

@app.get("/penjat/paraules/{tematica}", response_model=List[dict])
async def get_paraules_tematica(tematica: str):
    paraules = read_all(tematica)
    return paraules_sch.paraules_schema(paraules)

@app.get("/penjat/lletres/{idioma}", response_model=List[dict])
async def get_lletres(idioma: str):
    lletres = read_lletres_idioma(idioma)
    return paraules_sch.lletres_schema(lletres)