from fastapi import FastAPI
from schema.user import User, SignUp, Product

app =  FastAPI(
    title="FastAPI",
)

@app.post("/user")
def read_root(product: Product):
    print(product)
    return {"message": "Hello World"}

