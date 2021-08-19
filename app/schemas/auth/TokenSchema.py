from typing import Any, Dict
from pydantic import BaseModel

class TokenSchema(BaseModel):
    token: str
    type: str