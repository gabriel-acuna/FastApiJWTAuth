from typing import List
from app.models.core.modelos_principales import TipoDocenteLOES
from app.schemas.core.TipoDocenteLOESSchema import *


class ServicioTipoDocenteLOES():

    @classmethod
    async def listar(cls) -> List[TipoDocenteLOESSchema]:
        tipos_docentes: List[TipoDocenteLOESSchema] = []
        try:
            filas = await TipoDocenteLOES.listar()
            for fila in filas:
                tipos_docentes.append(TipoDocenteLOESSchema(**fila[0].__dict__))
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
        return tipos_docentes

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await TipoDocenteLOES.obtener(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def agregar_registro(cls, tipo_docente: TipoDocenteLOESPostSchema):
        try:
            return await TipoDocenteLOES.crear(tipo_docente=tipo_docente.tipo_docente)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def actualizar_registro(cls, tipo_docente: TipoDocenteLOESPutSchema):
        try:
            return await TipoDocenteLOES.actualizar(id=str(tipo_docente.id), tipo_docente=tipo_docente.tipo_docente)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await TipoDocenteLOES.eliminar(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def existe(cls, tipo_docente: TipoDocenteLOES) -> bool:
        try:
            existe = await TipoDocenteLOES.filtarPor(tipo_docente=tipo_docente.tipo_docente)
            if existe:
                return True
            return False
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
