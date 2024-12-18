from fastapi import FastAPI
from typing import List
import paraules_sch
from metodes_queries import read_tematiques, read_all, read_lletres_idioma, read_text_comencar, read_imatge_intents, read_partides_guanyades, read_info_joc

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

@app.get("/penjat/comencar_partida", response_model=dict)
async def get_comencar_partida():
    return paraules_sch.text_comencar_schema(read_text_comencar())

@app.get("/penjat/imatge_intents/{intents}", response_model=dict)
async def get_imatge_intents(intents: int):
    nom_imatge = read_imatge_intents(intents)
    return paraules_sch.imatge_intents_schema(nom_imatge)

@app.get("/penjat/usuaris/partides_guanyades/{nom_usuari}", response_model=dict)
async def get_partides_guanyades(nom_usuari: str):
    partides_guanyades = read_partides_guanyades(nom_usuari)
    return paraules_sch.partides_guanyades_schema(partides_guanyades)

@app.get("/penjat/joc/{id_joc}", response_model=dict)
async def get_info_joc(id_joc: int):
    joc = read_info_joc(id_joc)
    return paraules_sch.joc_schema(joc)