from pydantic import BaseModel

class MessageSchema(BaseModel):
    type:str
    content:str