import logging
from typing import List
from app.models.core.modelos_principales import NivelEducativo
from app.schemas.core.NivelEducativoSchema import *


class ServicioNivelEducativo():

    @classmethod
    async def listar(cls) -> List[NivelEducativoSchema]:
        nacionalidades: List[NivelEducativoSchema] = []
        try:
            filas = await NivelEducativo.listar()
            for fila in filas:
                nacionalidades.append(NivelEducativoSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return nacionalidades

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await NivelEducativo.obtener(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def agregar_registro(cls, nivel: NivelEducativoPostSchema):
        try:
            return await NivelEducativo.crear(nivel=nivel.nivel)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, nivel: NivelEducativoPutSchema):
        try:
            return await NivelEducativo.actualizar(id=str(nivel.id), nivel=nivel.nivel)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await NivelEducativo.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, nivel: NivelEducativo) -> bool:
        try:
            existe = await NivelEducativo.filtarPor(nivel=nivel.nivel)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
