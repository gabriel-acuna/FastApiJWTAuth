from app.models.core.modelos_principales import RelacionIES
from app.schemas.core.RelacionIESSchema import *
from typing import List

class ServicioRelacionIES():
    
    @classmethod
    async def listar(cls) -> List[RelacionIESSchema]:
        documentos: List[TipoDocumentoSchema] = []
        try:
            filas = await RelacionIES.listar()
            for fila in filas:
                documentos.append(RelacionIESSchema(**fila[0].__dict__))
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
        return documentos

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await RelacionIES.obtener(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def agregar_registro(cls, relacion: RelacionIESPostSchema):
        try:
            return await RelacionIES.crear(relacion=relacion.relacion)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def actualizar_registro(cls, relacion: RelacionIESPutSchema):
        try:
            return await RelacionIES.actualizar(id=str(relacion.id), relacion=relacion.relacion)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await RelacionIES.eliminar(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def existe(cls, relacion: RelacionIES) -> bool:
        try:
            existe = await RelacionIES.filtarPor(relacion=relacion.relacion)
            if existe:
                return True
            return False
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
