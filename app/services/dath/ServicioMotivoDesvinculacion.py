from typing import List
from app.schemas.dath.MotivoDesvinculacionSchema import *
from app.models.dath.modelos import MotivoDesvinculacion
import logging


class ServicioMotivoDesvinculacion():

    @classmethod
    async def listar(cls) -> List[MotivoDesvinculacionSchema]:
        motivos: List[MotivoDesvinculacionSchema] = []
        try:
            filas = await MotivoDesvinculacion.listar()
            for fila in filas:
                motivos.append(**fila[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return motivos

    @classmethod
    async def buscar_por_id(cls, id: str) -> MotivoDesvinculacionSchema:
        motivo: MotivoDesvinculacionSchema = None
        try:
            respuesta = await MotivoDesvinculacion.obtener(id)
            if respuesta:
                motivo = MotivoDesvinculacionSchema(respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return motivo

    @classmethod
    async def agregar_registro(cls, motivo: MotivoDesvinculacionPostSchema) -> bool:
        try:
            return await MotivoDesvinculacion.crear(
                motivo=motivo.motivo
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, motivo: MotivoDesvinculacionPutSchema):
        try:
            return await MotivoDesvinculacion.actualizar(
                id=motivo.id,
                motivo=motivo.motivo
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await MotivoDesvinculacion.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, motivo: MotivoDesvinculacionPostSchema) -> bool:
        try:
            existe = await MotivoDesvinculacion.filtarPor(motivo=motivo.motivo)
            return True if existe else False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
