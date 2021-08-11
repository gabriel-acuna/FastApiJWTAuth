from typing import List
from app.models.core.modelos_principales import Nacionalidad
from app.schemas.core.NacionalidadSchema import NacionalidadSchema, NacionalidadPostSchema, NacionalidadPutSchema


class ServicioNacionalidad():

    @classmethod
    async def listar(cls) -> List[NacionalidadSchema]:
        nacionalidades: List[NacionalidadSchema] = []
        try:
            filas = await Nacionalidad.listar()
            for fila in filas:
                nacionalidades.append(NacionalidadSchema(**fila[0].__dict__))
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
        return nacionalidades

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await Nacionalidad.obtener(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def agregar_registro(cls, nacionalidad: NacionalidadPostSchema):
        try:
            return await Nacionalidad.crear(nacionalidad=nacionalidad.nacionalidad)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def actualizar_registro(cls, nacionalidad: NacionalidadPutSchema):
        try:
            return await Nacionalidad.actualizar(id=str(nacionalidad.id), nacionalidad=nacionalidad.nacionalidad)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await Nacionalidad.eliminar(id)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def existe(cls, nacionalidad: Nacionalidad) -> bool:
        try:
            existe = await Nacionalidad.filtarPor(nacionalidad=nacionalidad.nacionalidad)
            if existe:
                return True
            return False
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
