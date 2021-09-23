import logging
from typing import List
from app.models.core.modelos_principales import TiempoDedicacionProfesor
from app.schemas.core.TiempoDedicacionProfesorSchema import *


class ServicioTiempoDedicacionProfesor():

    @classmethod
    async def listar(cls) -> List[TiempoDedicacionProfesorSchema]:
        documentos: List[TiempoDedicacionProfesorSchema] = []
        try:
            filas = await TiempoDedicacionProfesor.listar()
            for fila in filas:
                documentos.append(TiempoDedicacionProfesorSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return documentos

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await TiempoDedicacionProfesor.obtener(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def agregar_registro(cls, dedicacion: TiempoDedicacionProfesorPostSchema):
        try:
            return await TiempoDedicacionProfesor.crear(tiempo_dedicacion=dedicacion.tiempo_dedicacion)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, dedicacion: TiempoDedicacionProfesorPutSchema):
        try:
            return await TiempoDedicacionProfesor.actualizar(id=str(dedicacion.id), tiempo_dedicacion=dedicacion.tiempo_dedicacion)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await TiempoDedicacionProfesor.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, dedicacion: TiempoDedicacionProfesor) -> bool:
        try:
            existe = await TiempoDedicacionProfesor.filtarPor(tiempo_dedicacion=dedicacion.tiempo_dedicacion)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
