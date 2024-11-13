## IMPORTS ##
from fastapi import FastAPI, status, HTTPException 
from pydantic import BaseModel

## Declaro el basemodel per fer el POST:
class Usuari(BaseModel):
    nom: str
    cognom: str
    edat: int
    aula: str
    email: str
    sexe: str | None = None

app = FastAPI()

##GET que retorna un missatge de prova.
@app.get("/")
async def read_root():
    return {"message": "Prova de mètode GET"}

##GET que retorna un diccionari de 3 camps.
@app.get("/get2")
async def read_segonGet():
    return {
            "primer_camp": "hola",
            "segon_camp": "adeu",
            "tercer_camp": "últim"
            }

##Aquest POST agafa el BaseModel de dalt i el retorna. Els camps s'introdueixen al postman o al swagger per fer proves.
##També retorna un error introduit manualment mitjançant 'status_code'
@app.post("/introduirUsuari", status_code=status.HTTP_404_NOT_FOUND)
async def enter_user(usuari: Usuari):
    return usuari

##FUNCIÓ DE L'EXERCICI 7
usuaris = {
    "nom": str,
    "edat": int,
    "aula": str
}

@app.get("/usuaris/{cognom}")
async def read_cognom(cognom: str):
    if cognom not in usuaris:
        raise HTTPException(status_code=404, detail="No s'ha trobat el camp")
    return {"usuari": usuaris[cognom]}