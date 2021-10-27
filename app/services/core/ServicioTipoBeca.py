from app.schemas.core.TipoBecaSchema import *
from app.models.core.modelos_principales import TipoBeca
from typing import List
import logging


class ServicioTipoBeca():

    @classmethod
    async def listar(cls) -> List[TipoBecaSchema]:
        tipos_beca: List[TipoBecaSchema] = []
        try:
            filas = await TipoBeca.listar()
            if filas:
                for fila in filas:
                    tipos_beca.append(
                        fila[0].__dict__
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return tipos_beca

    @classmethod
    async def  buscar_por_id(cls, id:str) -> TipoBecaSchema:
        tipo_beca: TipoBecaSchema = None
        try:
            resultado = await TipoBeca.obtener(id)
            if resultado:
                tipo_beca = TipoBecaSchema(**resultado[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return tipo_beca

    @classmethod
    async def agregar_registro(cls, tipo_beca: TipoBecaPostSchema):
        try:
            return await TipoBeca.crear(
                tipo_beca=tipo_beca.tipo_beca,
                
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, tipo_beca: TipoBecaPutSchema):
        try:
            return await TipoBeca.actualizar(
                id=tipo_beca.id,
                tipo_beca=tipo_beca.tipo_beca,
                
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await TipoBeca.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, tipo_beca: TipoBecaPostSchema) -> bool:
        try:
            existe = await TipoBeca.filtarPor(tipo_beca=tipo_beca.tipo_beca)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)