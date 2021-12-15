from typing import List
from app.schemas.dath.RegimenLaboralSchema import *
from app.models.dath.modelos import RegimenLaboral
import logging


class ServicioRegimenLaboral():

    @classmethod
    async def listar(cls) -> List[RegimenLaboralSchema]:
        regimenes: List[RegimenLaboralSchema] = []
        try:
            filas = await RegimenLaboral.listar()
            for fila in filas:
                regimenes.append(RegimenLaboralSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return regimenes

    @classmethod
    async def buscar_por_id(cls, id: str) -> RegimenLaboralSchema:
        regimen: RegimenLaboralSchema = None
        try:
            respuesta = await RegimenLaboral.obtener(id)
            if respuesta:
                regimen = RegimenLaboralSchema(respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return regimen

    @classmethod
    async def agregar_registro(cls, regimen: RegimenLaboralPostSchema) -> bool:
        try:
            return await RegimenLaboral.crear(
                regimen=regimen.regimen
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, regimen: RegimenLaboralPutSchema):
        try:
            return await RegimenLaboral.actualizar(
                id=regimen.id,
                regimen=regimen.regimen
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await RegimenLaboral.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, regimen: RegimenLaboralPostSchema) -> bool:
        try:
            existe = await RegimenLaboral.filtarPor(regimen=regimen.regimen)
            return True if existe else False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
