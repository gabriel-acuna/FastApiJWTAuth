from app.schemas.cv.ExperienciaLaboralSchema import *
from app.models.cv.modelos import ExperienciaLaboral
from typing import List
import logging


class ServicoExperienciaLoboral():

    @classmethod
    async def listar(cls, id_persona: str) -> List[ExperienciaLaboralSchema]:
        experiencias: List[ExperienciaLaboralSchema] = []

        try:
            filas = await ExperienciaLaboral.filtarPor(id_persona=id_persona)
            for fila in filas:
                experiencias.append(fila[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return experiencias

    @classmethod
    async def buscar_por_id(cls, id: str) -> ExperienciaLaboralSchema:
        experiencia: ExperienciaLaboralSchema = None
        try:
            respuesta = await ExperienciaLaboral.obtener(id=id)
            if respuesta:
                experiencia = ExperienciaLaboralSchema(
                    respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return experiencia

    @classmethod
    async def agregar_registro(cls, experiencia: ExperienciaLaboralPostSchema):

        try:
            return await ExperienciaLaboral.crear(
                id_persona=experiencia.id_persona,
                empresa=experiencia.empresa,
                lugar=experiencia.lugar,
                cargo=experiencia.cargo,
                inicio=experiencia.inicio,
                fin=experiencia.fin
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, experiencia: ExperienciaLaboralPutSchema):
        try:
            return await ExperienciaLaboral.actualizar(
                id=experiencia.id,
                empresa=experiencia.empresa,
                lugar=experiencia.lugar,
                cargo=experiencia.cargo,
                inicio=experiencia.inicio,
                fin=experiencia.fin

            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await ExperienciaLaboral.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, experiencia: ExperienciaLaboralPostSchema) -> bool:
        try:
            existe = await ExperienciaLaboral.filtarPor(
                id_persona=experiencia.id_persona,
                empresa=experiencia.empresa,
                inicio=experiencia.inicio

            )
            if existe:
                return True
            return False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
