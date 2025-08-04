from typing import Optional
from fastapi import APIRouter, Header
from pydantic import BaseModel

book_router = APIRouter()

@book_router.get("/")
def read_root():
    return {"message": "Hello World"}


@book_router.get("/user")
def get_user(name: str) -> dict:
    return {"message": f"Hello {name}"}


@book_router.get("/greet")
def greet(name: Optional[str] = "Zain", age: int = 20) -> dict:
    return {"message": f"Hello {name}", "age": age}


class CreateBookModel(BaseModel):
    title: str
    author: str

@book_router.post("/create-book")
def create_book(book_data: CreateBookModel)-> dict:
    return {
        "title": book_data.title,
        "author": book_data.author
    }


@book_router.get("/get-header")
def get_header(
    accept: str = Header(None)
):
    request_header = {}

    request_header["Accept"] = accept
    return request_header