from app.schemas.core.GradoSchema import *
from app.models.core.modelos_principales import Grado
from typing import List
import logging


class ServicioGrado():

    @classmethod
    async def listar(cls) -> List[GradoSchema]:
        grados: List[GradoSchema] = []
        try:
            filas = await Grado.listar()
            if filas:
                for fila in filas:
                    grados.append(
                        fila[0].__dict__
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return grados

    @classmethod
    async def  buscar_por_id(cls, id:str) -> GradoSchema:
        grado: GradoSchema = None
        try:
            resultado = await Grado.obtener(id)
            if resultado:
                grado = GradoSchema(**resultado[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return grado

    @classmethod
    async def agregar_registro(cls, grado: GradoPostSchema):
        try:
            return await Grado.crear(
                grado=grado.grado,
                
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, grado: GradoPutSchema):
        try:
            return await Grado.actualizar(
                id=grado.id,
                grado=grado.grado,
                
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await Grado.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, grado: GradoPostSchema) -> bool:
        try:
            existe = await Grado.filtarPor(grado=grado.grado)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)