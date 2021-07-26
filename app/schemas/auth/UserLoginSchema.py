from pydantic import BaseModel, Field, EmailStr

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "g.acuna@mail.com",
                "password": "G.Pj_67893Q"
            }
        }