from typing import List
from app.schemas.dath.ModalidadContractualSchema import *
from app.models.dath.modelos import ModalidadContractual
import logging


class ServicioModalidadContractual():

    @classmethod
    async def listar(cls) -> List[ModalidadContractualSchema]:
        modalidades: List[ModalidadContractualSchema] = []
        try:
            filas = await ModalidadContractual.listar()
            for fila in filas:
                modalidades.append(**fila[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return modalidades

    @classmethod
    async def buscar_por_id(cls, id: str) -> ModalidadContractualSchema:
        modalidad: ModalidadContractualSchema = None
        try:
            respuesta = await ModalidadContractual.obtener(id)
            if respuesta:
                modalidad = ModalidadContractualSchema(respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return modalidad

    @classmethod
    async def agregar_registro(cls, modalidad: ModalidadContractualPostSchema) -> bool:
        try:
            return await ModalidadContractual.crear(
                modalidad=modalidad.modalidad
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, modalidad: ModalidadContractualPutSchema):
        try:
            return await ModalidadContractual.actualizar(
                id=modalidad.id,
                modalidad=modalidad.modalidad
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await ModalidadContractual.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, modalidad: ModalidadContractualPostSchema) -> bool:
        try:
            existe = await ModalidadContractual.filtarPor(modalidad=modalidad.modalidad)
            return True if existe else False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
