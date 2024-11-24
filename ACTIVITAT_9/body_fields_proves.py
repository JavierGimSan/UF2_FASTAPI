from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    nom: str
    descripcio: str | None = Field(
        default=None, title="Descripció de prova", max_length=20
    )
    preu: float = Field(gt=0, descripcio="El preu ha de ser major que zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
