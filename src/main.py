from fastapi import FastAPI
from src.router.book_route import book_router
from contextlib import asynccontextmanager
from src.db.db import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is running")
    await init_db()

    yield

    print("Server is stopped")


# 1. Create a FastAPI instance
version = "v1"
app = FastAPI(
    version=version,
    lifespan=life_span
)



app.include_router(book_router, prefix=f"/api/{version}/book", tags=["Books"])