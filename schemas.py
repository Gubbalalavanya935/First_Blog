from typing import List, Optional
from pydantic import BaseModel


# -------- BLOG --------

class Blog(BaseModel):
    title: str
    body: str
    user_id: int

    class Config:
        from_attributes = True


class ShowBlog(BaseModel):
    title: str
    body: str

    class Config:
        from_attributes = True


# -------- USER --------

class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[ShowBlog] = []

    class Config:
        from_attributes = True


# -------- AUTH --------

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None






