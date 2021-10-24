from app.models.cv.modelos import Ponencia
from app.schemas.cv.PonenciaSchema import *
import logging

from typing import List

class ServicioCapacitacionFacilitador():

    @classmethod
    async def listar(cls, id_persona: str) -> List[PonenciaSchema]:
        ponencias: List[PonenciaSchema] = []

        try:
            filas = await Ponencia.filtarPor(id_persona=id_persona)
            for fila in filas:
                ponencias.append(fila[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return ponencias

    @classmethod
    async def buscar_por_id(cls, id: str) -> PonenciaSchema:
        ponencia: PonenciaSchema = None

        try:
            respuesta = await Ponencia.obtener(id=id)
            if respuesta:
                ponencia = PonenciaSchema(
                    respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return ponencia

    @classmethod
    async def agregar_registro(cls, ponencia: PonenciaPostSchema):

        try:
            return await Ponencia.crear(
                id_persona=ponencia.id_persona,
                tema=ponencia.tema,
                institucion_organizadora=ponencia.institucion_organizadora,
                evento=ponencia.evento,
                caracter=ponencia.caracter,
                lugar=ponencia.lugar,
                fecha=ponencia.fecha
    
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, ponencia: PonenciaPutSchema):
        try:
            return await Ponencia.actualizar(
                id=ponencia.id,
                tema=ponencia.tema,
                institucion_organizadora=ponencia.institucion_organizadora,
                evento=ponencia.evento,
                caracter=ponencia.caracter,
                lugar=ponencia.lugar,
                fecha=ponencia.fecha
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await Ponencia.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, ponencia: PonenciaPostSchema) -> bool:
        try:
            existe = await Ponencia.filtarPor(
                id_persona = ponencia.id_persona,
                tema = ponencia.tema,
                institucion_organizadora = ponencia.institucion_organizadora,
                lugar = ponencia.lugar,
                fecha = ponencia.fecha

            )
            if existe:
                return True
            return False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
