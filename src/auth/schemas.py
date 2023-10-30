from ast import List
from enum import Enum
from typing import Optional


from datetime import datetime, date

from fastapi_users import schemas

from pydantic import EmailStr
from typing import Literal

from pydantic import BaseModel
 

class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    gender: Literal["w", "m"]
    first_name: str
    last_name: str
    patronymic: str
    date_of_birth: date
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    sub_id: Optional[int]
    trainer_id: Optional[int]

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    gender: Literal["w", "m"]
    first_name: str
    last_name: str
    patronymic: str
    date_of_birth: date
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    sub_id: Optional[int]
    trainer_id: Optional[int]

    # trainer_id: Optional[int]
    # sub: Optional["SubscriptionTypeBase"]

class UserUpdate(schemas.BaseUserUpdate):
    gender: Literal["w", "m"] 
    first_name: str 
    last_name: str 
    patronymic: str
    date_of_birth: date
    sub_id: Optional[int]
    trainer_id: Optional[int]