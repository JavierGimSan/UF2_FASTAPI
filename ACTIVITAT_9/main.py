from fastapi import FastAPI
from typing import List
import schemas.users_sch as users_sch
import crud.users as users

app = FastAPI()

@app.get("/users", response_model=List[dict])
async def get_users():
    return users_sch.users_schema(users.read_users())