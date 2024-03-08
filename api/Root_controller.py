from fastapi import FastAPI
from user import User, Gender, Role
from typing import List
from uuid import uuid4


myapp = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="ABC",
        last_name="DEF",
        gender=Gender.male,
        role=[Role.student, Role.user]
    ),
    User(
        id=uuid4(),
        first_name="PQR",
        last_name="XYZ",
        gender=Gender.female,
        role=[Role.student, Role.user]
    )
]


@myapp.get("/")
async def root():
    return "Hello World"


@myapp.get("/api/v1/alluser")
async def list_users():
    return db


@myapp.post("/api/v1/adduser")
async def add_users(user: User):
    db.append(user)
