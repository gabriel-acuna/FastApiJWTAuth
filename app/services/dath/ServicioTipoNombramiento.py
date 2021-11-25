from typing import List
from app.schemas.dath.TipoNombramientoSchema import *
from app.models.dath.modelos import TipoNombramiento
import logging


class ServicioTipoNombramiento():

    @classmethod
    async def listar(cls) -> List[TipoNombramientoSchema]:
        nombramientos: List[TipoNombramientoSchema] = []
        try:
            filas = await TipoNombramiento.listar()
            for fila in filas:
                nombramientos.append(**fila[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return nombramientos

    @classmethod
    async def buscar_por_id(cls, id: str) -> TipoNombramientoSchema:
        nombramiento: TipoNombramientoSchema = None
        try:
            respuesta = await TipoNombramiento.obtener(id)
            if respuesta:
                nombramiento = TipoNombramientoSchema(respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return nombramiento

    @classmethod
    async def agregar_registro(cls, nombramiento: TipoNombramientoPostSchema) -> bool:
        try:
            return await TipoNombramiento.crear(
                nombramiento=nombramiento.nombramiento
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, nombramiento: TipoNombramientoPutSchema):
        try:
            return await TipoNombramiento.actualizar(
                id=nombramiento.id,
                nombramiento=nombramiento.nombramiento
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await TipoNombramiento.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, nombramiento: TipoNombramientoPostSchema) -> bool:
        try:
            existe = await TipoNombramiento.filtarPor(nombramiento=nombramiento.nombramiento)
            return True if existe else False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
