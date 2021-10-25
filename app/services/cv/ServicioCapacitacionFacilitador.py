from typing import List
from app.models.cv.modelos import CapacitacionFacilitador
from app.schemas.cv.CapacitacionFacilitardorSchema import *
import logging


class ServicioCapacitacionFacilitador():

    @classmethod
    async def listar(cls, id_persona: str) -> List[CapacitacionFacilitadorSchema]:
        capacitaciones: List[CapacitacionFacilitadorSchema] = []

        try:
            filas = await CapacitacionFacilitador.filtarPor(id_persona=id_persona)
            for fila in filas:
                capacitaciones.append(fila[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return capacitaciones

    @classmethod
    async def buscar_por_id(cls, id: str) -> CapacitacionFacilitadorSchema:
        capacitacion: CapacitacionFacilitadorSchema = None

        try:
            respuesta = await CapacitacionFacilitador.obtener(id=id)
            if respuesta:
                capacitacion = CapacitacionFacilitadorSchema(
                    **respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return capacitacion

    @classmethod
    async def agregar_registro(cls, capacitacion: CapacitacionFacilitadorPostSchema):

        try:
            return await CapacitacionFacilitador.crear(
                id_persona=capacitacion.id_persona,
                funcion_evento=capacitacion.funcion_evento,
                institucion_organizadora=capacitacion.institucion_organizadora,
                lugar=capacitacion.lugar,
                horas=capacitacion.horas,
                inicio=capacitacion.inicio,
                fin=capacitacion.fin,
                certificado=capacitacion.certificado
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, capacitacion: CapacitacionFacilitadorPutSchema):
        try:
            return await CapacitacionFacilitador.actualizar(
                id=capacitacion.id,
                funcion_evento=capacitacion.funcion_evento,
                institucion_organizadora=capacitacion.institucion_organizadora,
                lugar=capacitacion.lugar,
                horas=capacitacion.horas,
                inicio=capacitacion.inicio,
                fin=capacitacion.fin,
                certificado=capacitacion.certificado
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await CapacitacionFacilitador.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, capacitacion: CapacitacionFacilitadorPostSchema) -> bool:
        try:
            existe = await CapacitacionFacilitador.filtarPor(
                id_persona = capacitacion.id_persona,
                funcion_evento = capacitacion.funcion_evento,
                institucion_organizadora = capacitacion.institucion_organizadora,
                inicio = capacitacion.inicio,
                fin = capacitacion.fin

            )
            if existe:
                return True
            return False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
