from typing import List
from app.models.core.modelos_principales import TipoEscalafonNombramiento
from app.schemas.core.TipoEscalafonNombramientoSchema import *


class ServicioTipoEscalafonNombramiento():

    @classmethod
    async def listar(cls) -> List[TipoEscalafonNombramientoSchema]:
        esclafones: List[TipoEscalafonNombramientoSchema] = []
        try:
            filas = await TipoEscalafonNombramiento.listar()
            for fila in filas:
                esclafones.append(TipoEscalafonNombramientoSchema(**fila[0].__dict__))
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
        return esclafones

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await TipoEscalafonNombramiento.obtener(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def agregar_registro(cls, tipo_escalafon: TipoEscalafonNombramientoPostSchema):
        try:
            return await TipoEscalafonNombramiento.crear(escalafon_nombramiento=tipo_escalafon.escalafon_nombramiento)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def actualizar_registro(cls, tipo_escalafon: TipoEscalafonNombramientoPutSchema):
        try:
            return await TipoEscalafonNombramiento.actualizar(id=str(tipo_escalafon.id), escalafon_nombramiento=tipo_escalafon.escalafon_nombramiento)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await TipoEscalafonNombramiento.eliminar(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def existe(cls, tipo_escalafon: TipoEscalafonNombramiento) -> bool:
        try:
            existe = await TipoEscalafonNombramiento.filtarPor(escalafon_nombramiento=tipo_escalafon.escalafon_nombramiento)
            if existe:
                return True
            return False
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
