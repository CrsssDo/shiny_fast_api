import pydantic
from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id:int
    name: Optional[str] = None
    email:Optional[str] = None
    pass_word: Optional[str] = None
    is_verified: Optional[bool] = False
    image_url: Optional[str] = None

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str 
    pass_word: str 

    class Config:
        orm_mode = True