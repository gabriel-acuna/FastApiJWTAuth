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
            print(f"Ha ocurrido una excepción {ex}")
        return discapacidades

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await Discapacidad.obtener(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def agregar_registro(cls, discapacidad: DiscapacidadPostSchema):
        try:
            return await Discapacidad.crear(discapacidad=discapacidad.discapacidad)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def actualizar_registro(cls, discapacidad: DiscapacidadPutSchema):
        try:
            return await Discapacidad.actualizar(id=str(discapacidad.id), discapacidad=discapacidad.discapacidad)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await Discapacidad.eliminar(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def existe(cls, discapacidad: Discapacidad) -> bool:
        try:
            existe = await Discapacidad.filtarPor(discapacidad = discapacidad.discapacidad)
            if existe:
                return True
            return False

        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
