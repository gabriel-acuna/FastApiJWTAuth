from app.models.cv.modelos import MeritoDistincion
from app.schemas.cv.MeritoDistincionSchema import *
from typing import List
import logging

class ServicioMerito():
    @classmethod
    async def listar(cls, id_persona: str) -> List[MeritoDistincionSchema]:
        meritos: List[MeritoDistincionSchema] = []

        try:
            filas = await MeritoDistincion.filtarPor(id_persona=id_persona)
            for fila in filas:
                meritos.append(fila[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return meritos

    @classmethod
    async def buscar_por_id(cls, id: str) -> MeritoDistincionSchema:
        merito: MeritoDistincionSchema = None

        try:
            respuesta = await MeritoDistincion.obtener(id=id)
            if respuesta:
                merito = MeritoDistincionSchema(
                    respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return merito

    @classmethod
    async def agregar_registro(cls, merito: MeritoDistincionPostSchema):

        try:
            return await MeritoDistincion.crear(
                id_persona=merito.id_persona,
                titulo = merito.titulo,
                institucion_asupiciante = merito.institucion_asupiciante,
                funcion = merito.funcion,
                fecha_inicio = merito.fecha_inicio,
                fecha_fin = merito.fecha_fin
                
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, merito: MeritoDistincionPutSchema):
        try:
            return await MeritoDistincion.actualizar(
                id=merito.id,
                titulo = merito.titulo,
                institucion_asupiciante = merito.institucion_asupiciante,
                funcion = merito.funcion,
                fecha_inicio = merito.fecha_inicio,
                fecha_fin = merito.fecha_fin
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await MeritoDistincion.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, merito: MeritoDistincionPostSchema) -> bool:
        try:
            existe = await MeritoDistincion.filtarPor(
                id_persona = merito.id_persona,
                titulo = merito.titulo,
                institucion_asupiciante = merito.institucion_asupiciante,
                funcion = merito.funcion,
                fecha_inicio = merito.fecha_inicio,

            )
            if existe:
                return True
            return False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)