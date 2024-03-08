from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum


class Role(str, Enum):
    admin = "admin"
    student = "student"
    user = "user"


class Gender(str, Enum):
    male = "male"
    female = "female"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    middle_name: Optional[str]
    last_name: str
    gender: Gender
    role: List[Role]
