from pydantic import BaseModel, Field, model_validator, computed_field

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=10, max_length=50)


class SignUp(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def signup(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Password and confirm password do not match")
        return values

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity