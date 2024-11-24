from pydantic import BaseModel

def user_schema(user) -> dict:
    return {"id": user[0],
            "name": user[1],
            "surname": user[2],
            }

def users_schema(users) -> dict:
    return [user_schema(user) for user in users]

class CrearUsuari(BaseModel):
    name: str
    surname: str

class ActualitzaUsuari(BaseModel):
    name: str
    surname: str