from fastapi import FastAPI, status
from pydantic import BaseModel

##Declaro el basemodel per fer el POST:
class Usuari(BaseModel):
    nom: str
    cognom: str
    edat: int
    aula: str
    email: str
    sexe: str | None = None

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Prova de mètode GET"}

@app.get("/get2")
async def read_segonGet():
    return {
            "primer_camp": "hola",
            "segon_camp": "adeu",
            "tercer_camp": "últim"
            }

@app.post("/introduirUsuari", status_code=status.HTTP_404_NOT_FOUND)
async def enter_user(usuari: Usuari):
    return usuari