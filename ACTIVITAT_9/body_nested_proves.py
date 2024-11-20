from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Carta(BaseModel):
    contingut: str
    color_tinta: str

class Sobre(BaseModel):
    nom: str
    forma: str
    remitent: str
    carta: Carta


@app.put("/sobre/{sobre_id}")
async def update_sobre(sobre_id: int, sobre: Sobre):
    results = {"sobre_id": sobre_id, "sobre": sobre}
    return results
