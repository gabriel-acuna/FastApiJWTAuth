from typing import List
from app.schemas.dath.TipoContratoSchema import TipoContratoPostSchema, TipoContratoPutSchema, TipoContratoSchema
from app.models.dath.modelos import TipoContrato
import logging


class ServicioTipoContrato():

    @classmethod
    async def listar(cls) -> List[TipoContratoSchema]:
        contratos: List[TipoContratoSchema] = []
        try:
            filas = await TipoContrato.listar()
            for fila in filas:
                contratos.append(**fila[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return contratos

    @classmethod
    async def buscar_por_id(cls, id: str) -> TipoContratoSchema:
        contrato: TipoContratoSchema = None
        try:
            respuesta = await TipoContrato.obtener(id)
            if respuesta:
                contrato = TipoContratoSchema(respuesta[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return contrato

    @classmethod
    async def agregar_registro(cls, contrato: TipoContratoPostSchema) -> bool:
        try:
            return await TipoContrato.crear(
                contrato=contrato.contrato
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, contrato: TipoContratoPutSchema):
        try:
            return await TipoContrato.actualizar(
                id=contrato.id,
                contrato=contrato.contrato
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await TipoContrato.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, contrato: TipoContratoPostSchema) -> bool:
        try:
            existe = await TipoContrato.filtarPor(contrato=contrato.contrato)
            return True if existe else False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
