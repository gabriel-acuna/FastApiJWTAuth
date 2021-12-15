from app.schemas.dath.EvaluacionPersonalSchema import *
from app.models.dath.modelos import EvaluacionPersonal
from typing import List
import logging


class ServicioEvaluacionPersonal():

    @classmethod
    async def listar_por_persona(cls, id_persona: str) -> List[EvaluacionPersonalSchema]:
        evaluaciones: List[EvaluacionPersonalSchema] = []
        try:
            filas = await EvaluacionPersonal.filtarPor(id_persona=id_persona)
            for fila in filas:
                evaluaciones.append(
                    EvaluacionPersonalSchema(EvaluacionPersonalSchema(**fila[0].__dict__))
                )

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return evaluaciones

    @classmethod
    async def buscar_por_id(cls, id: str) -> EvaluacionPersonalSchema:
        evaluacion: EvaluacionPersonalSchema = None
        try:
            resultado = await EvaluacionPersonal.obtener(id)
            if resultado:
                evaluacion = EvaluacionPersonalSchema(**resultado.__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return evaluacion

    @classmethod
    async def agregar_registro(cls, evaluacion: EvaluacionPersonalPostSchema) -> bool:
        try:
            return await EvaluacionPersonal.crear(
                id_persona=evaluacion.id_persona,
                desde=evaluacion.desde,
                hasta=evaluacion.hasta,
                puntaje=evaluacion.puntaje,
                calificaion=evaluacion.calificacion
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, evaluacion: EvaluacionPersonalPutSchema) -> bool:
        try:
            return await EvaluacionPersonal.crear(
                id=evaluacion.id,
                id_persona=evaluacion.id_persona,
                desde=evaluacion.desde,
                hasta=evaluacion.hasta,
                puntaje=evaluacion.puntaje,
                calificaion=evaluacion.calificacion
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await EvaluacionPersonal.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, evaluacion: EvaluacionPersonalPostSchema) -> bool:
        try:
            existe = await EvaluacionPersonal.filtarPor(
                id_persona=evaluacion.id_persona,
                desde= evaluacion.desde,
                hasta = evaluacion.hasta
                )
            return True if existe else False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
