from typing import List
from app.models.core.modelos_principales import IESNacional
from app.schemas.core.IESNacionalSchema import *
import logging


class ServicioIES():

    @classmethod
    async def listar(cls) -> List[IESNacionalSchema]:
        ies_nacionales: List[IESNacionalSchema] = []
        try:
            filas = await IESNacional.listar()
            if filas:
                for fila in filas:
                    ies_nacionales.append(
                        fila[0].__dict__
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return ies_nacionales

    @classmethod
    async def buscar_por_id(cls, id: str) -> IESNacionalSchema:
        ies: IESNacionalSchema = None

        try:
            respuesta = await IESNacional.obtener(id=id)
            if respuesta:
                ies = IESNacionalSchema(
                    **respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return ies

    @classmethod
    async def agregar_registro(cls, ies: IESNacionalPostSchema):

        try:
            return await IESNacional.crear(
                codigo=ies.codigo,
                institucion=ies.institucion
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, ies: IESNacionalPutSchema):
        try:
            return await IESNacional.actualizar(
                id=ies.id,
                codigo=ies.codigo,
                institucion=ies.institucion
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str)->bool:
        try:
            return await IESNacional.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, ies: IESNacionalPostSchema) -> bool:
        try:
            existe = await ies.filtarPor(
                institucion=ies.institucion

            )
            if existe:
                return True
            return False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
