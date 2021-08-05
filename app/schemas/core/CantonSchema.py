from pydantic import BaseModel

class CantonSchema(BaseModel):
    id:int
    canton:str
    provincia_id: str