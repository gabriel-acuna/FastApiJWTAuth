from datetime import date
from pydantic import BaseModel

class PeriodoAcademicoSchema(BaseModel):
    id: int
    nombre: str
    inicio: date
    fin: date
    activo: bool