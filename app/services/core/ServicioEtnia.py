import logging
from typing import List
from app.models.core.modelos_principales import Etnia
from app.schemas.core.EtniaSchema import EtniaSchema, EtniaPostSchema, EtniaPutSchema


class ServicioEtnia():

    @classmethod
    async def listar(cls) -> List[EtniaSchema]:
        etnias: List[EtniaSchema] = []
        try:
            filas = await Etnia.listar()
            for fila in filas:
                etnias.append(EtniaSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return etnias

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await Etnia.obtener(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def agregar_registro(cls, etnia: EtniaPostSchema):
        try:
            return await Etnia.crear(etnia=etnia.etnia)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, etnia: EtniaPutSchema):
        try:
            return await Etnia.actualizar(id=str(etnia.id), etnia=etnia.etnia)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await Etnia.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, etnia: Etnia) -> bool:
        try:
            existe = await Etnia.filtarPor(etnia = etnia.etnia)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
