from app.models.core.modelos_principales import FinanciamientoBeca
from app.schemas.core.FinanciamientoBecaSchema import *
import logging
from typing import List


class ServicioFinanciamiento():

    @classmethod
    async def listar(cls) -> List[FinanciamientoBecaSchema]:
        financiamientos: List[FinanciamientoBecaSchema] = []
        try:
            filas = await FinanciamientoBeca.listar()
            if filas:
                for fila in filas:
                    financiamientos.append(
                        fila[0].__dict__
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return financiamientos

    @classmethod
    async def  buscar_por_id(cls, id:str) -> FinanciamientoBecaSchema:
        financiamiento: FinanciamientoBecaSchema = None
        try:
            resultado = await FinanciamientoBeca.obtener(id)
            if resultado:
                financiamiento = FinanciamientoBecaSchema(**resultado[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return financiamiento

    @classmethod
    async def agregar_registro(cls, financiamiento: FinanciamientoBecaPostSchema):
        try:
            return await FinanciamientoBeca.crear(
                financiamiento=financiamiento.financiamiento,
                
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, financiamiento: FinanciamientoBecaPutSchema):
        try:
            return await FinanciamientoBeca.actualizar(
                id=financiamiento.id,
                financiamiento=financiamiento.financiamiento,
                
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await FinanciamientoBeca.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, financiamiento: FinanciamientoBecaPostSchema) -> bool:
        try:
            existe = await FinanciamientoBeca.filtarPor(financiamiento=financiamiento.financiamiento)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)