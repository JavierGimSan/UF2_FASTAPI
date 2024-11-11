from fastapi import FastAPI

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

