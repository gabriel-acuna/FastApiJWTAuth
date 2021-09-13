from typing import List
from app.models.core.modelos_principales import EstructuraInstitucional
from app.schemas.core.EstructuraInstitucionalSchema import *


class ServicioEtnia():

    @classmethod
    async def listar(cls) -> List[EstructuraInstitucionalSchema]:
        etnias: List[EstructuraInstitucionalSchema] = []
        try:
            filas = await EstructuraInstitucional.listar()
            for fila in filas:
                etnias.append(EstructuraInstitucionalSchema(**fila[0].__dict__))
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
        return etnias

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await EstructuraInstitucional.obtener(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def agregar_registro(cls, estructura: EstructuraInstitucionalPostSchema):
        try:
            return await EstructuraInstitucional.crear(
                documento_aprobacion = estructura.documento_aprobacion,
                fecha_aprobacion = estructura.fecha_aprobacion
            )
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def actualizar_registro(cls, estructura: EstructuraInstitucionalPutSchema):
        try:
            return await EstructuraInstitucional.actualizar(
                id= estructura.id,
                documento_aprobacion = estructura.documento_aprobacion,
                fecha_aprobacion = estructura.fecha_aprobacion
                )
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await EstructuraInstitucional.eliminar(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def existe(cls, estructura: EstructuraInstitucionalSchema) -> bool:
        try:
            existe = await EstructuraInstitucional.filtarPor(documento_aprobacion = estructura.documento_aprobacion)
            if existe:
                return True
            return False
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
