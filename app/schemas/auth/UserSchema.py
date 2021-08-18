from pydantic import BaseModel, Field, EmailStr

class UserPostSchema(BaseModel):
    primer_nombre: str = Field(...)
    segundo_nombre: str = Field(...) 
    primer_apellido: str = Field(...)
    segundo_apellido: str = Field(...)
    email: EmailStr = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "primer_nombre": "Gabriel",
                "segundo_nombre": "Stefano",
                "primer_apellido":"Acuña",
                "segundo_apellido": "Regalado",
                "email": "g.acuna@mail.com"
               
            }
        }