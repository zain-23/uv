from fastapi import FastAPI
from router.book_route import book_router

# 1. Create a FastAPI instance
version = "v1"
app = FastAPI(
    version=version
)



app.include_router(book_router, prefix=f"/api/{version}/book", tags=["Books"])