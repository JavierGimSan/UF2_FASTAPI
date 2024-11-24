from fastapi import FastAPI
from typing import List
import users_sch
import users

app = FastAPI()

@app.get("/users", response_model=List[dict])
async def get_users():
    return users_sch.users_schema(users.read_users())