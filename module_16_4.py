from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users")
async def all_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def add_user(user: User, username: str, age: int) -> str:
    if len(users) == 0:
        user.id = 1
    else:
        added_user = users[-1]
        user.id = added_user.id + 1
    user.username = username
    user.age = age
    users.append(user)
    return f'User id: {user.id}, username: {user.username}, age: {user.age} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(description='Enter User ID', example=1)],
                      username: Annotated[str, Path(min_length=5,max_length=20,description="Enter username",example='username')],
                      age: Annotated[int,Path(ge=18,le=120,description="Enter age",example='24')]) -> str:
    found = 1
    for obj in users:
        if getattr(obj, 'id') == user_id:
            updated_user = obj
            found = 0
            break
    if found == 0:
        updated_user.username = username
        updated_user.age = age
        return f'User {user_id}  was updated'
    else:
        raise HTTPException(status_code=404,detail=f'User {user_id} not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id: int = Path(description='Enter User ID', example=1)) -> str:
    found = 1
    for obj in users:
        if getattr(obj, 'id') == user_id:
            deleted_user = obj
            found = 0
            break
    if found == 0:
        users.remove(deleted_user)
        return f'User {user_id}  was updated'
    else:
        raise HTTPException(status_code=404, detail=f'User {user_id} not found')