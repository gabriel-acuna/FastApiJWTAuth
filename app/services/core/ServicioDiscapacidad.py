from typing import List
from app.models.core.modelos_principales import Discapacidad
from app.schemas.core.DiscapacidadSchema import DiscapacidadPostSchema, DiscapacidadPutSchema, DiscapacidadSchema


class ServicioDiscapacidad():
    

    @classmethod
    async def listar(cls) -> List[DiscapacidadSchema]:
        discapacidades: List[DiscapacidadSchema] = []
        try:
            filas = await Discapacidad.listar()
            for fila in filas:
                discapacidades.append(DiscapacidadSchema(**fila[0].__dict__))
        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")
        return discapacidades

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await Discapacidad.obtener(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")

    @classmethod
    async def agregar_registro(cls, discapacidad: DiscapacidadPostSchema):
        try:
            return await Discapacidad.crear(discapacidad)
        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")

    @classmethod
    async def actualizar_registro(cls, discapacida: DiscapacidadPutSchema):
        try:
            return await Discapacidad.actualizar(discapacida.__dict__)
        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")

    @classmethod
    async def eliminar_registro(cls, id: int):
        try:
            eliminado = await cls.__discapacidad.eliminar(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepcion {ex}")
