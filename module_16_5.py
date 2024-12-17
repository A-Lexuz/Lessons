from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True})
templates = Jinja2Templates(directory="16/templates")
users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/")
async def all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get(path="/user/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

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
