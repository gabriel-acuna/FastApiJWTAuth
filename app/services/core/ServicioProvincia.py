import logging

from sqlalchemy.sql.expression import true
from app.schemas.core.CantonSchema import CantonSchema
from typing import List
from app.models.core.modelos_principales import Canton, Provincia
from app.schemas.core.ProvinciaSchema import *


class ServicioProvincia():

    @classmethod
    async def listar(cls) -> List[ProvinciaSchema]:
        provincias: List[ProvinciaSchema] = []
        try:
            filas = await Provincia.listar()
            for fila in filas:
                provincias.append(ProvinciaSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return provincias

    @classmethod
    async def buscar_por_id(cls, id: int) -> ProvinciaSchema:
        provincia: ProvinciaSchema = None
        try:
            resultado = await Provincia.obtener(id)
            if resultado:
                provincia = ProvinciaSchema(resultado[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return provincia

    @classmethod
    async def listar_cantones_por_provincia(cls, id_provincia: int) -> List[CantonSchema]:
        cantones: List[CantonSchema] = []
        try:
            filas = await Canton.filtarPor(provincia_id=id_provincia)
            for fila in filas:
                cantones.append(CantonSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return cantones

    @classmethod
    async def agregar_registro(cls, provincia: ProvinciaPostSchema) -> bool:
        try:
            return await Provincia.crear(
                provincia = provincia.provincia
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    
    @classmethod
    async def actualizar_registro(cls, provincia: ProvinciaPutSchema) -> bool:
        try:
            return await Provincia.actualizar(
                id = provincia.id,
                provincia = provincia.provincia
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: int):
        try:
            return await ServicioProvincia.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, provincia: ProvinciaPostSchema) -> bool:
        try:
            existe =  await Provincia.filtarPor(
                provincia = provincia.provincia
            )
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
