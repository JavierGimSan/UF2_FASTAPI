from fastapi import FastAPI, HTTPException
from typing import List
import schemas.users_sch as users_sch
from crud.users import read_users, create_user, update_user, delete_user
from schemas.users_sch import CrearUsuari, ActualitzaUsuari

app = FastAPI()

@app.get("/users", response_model=List[dict])
async def get_users():
    return users_sch.users_schema(read_users())

@app.post("/users", response_model=dict)
async def add_user(user: CrearUsuari):
    try:
        user_id = create_user(user.name, user.surname)
        return {"id": user_id, "name": user.name, "surname": user.surname}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.put("/users/{user_id}", response_model=dict)
async def modify_user(user_id: int, user: ActualitzaUsuari):
    try:
        message = update_user(user_id, user.name, user.surname)
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/users/{user_id}", response_model=dict)
async def remove_user(user_id: int):
    try:
        message = delete_user(user_id)
        return {"message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
