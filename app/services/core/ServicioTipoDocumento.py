import logging
from typing import List
from app.models.core.modelos_principales import TipoDocumento
from app.schemas.core.TipoDocumentoSchema import TipoDocumentoSchema, TipoDocumentoPostSchema, TipoDocumentoPutSchema


class ServicioTipoDocumento():

    @classmethod
    async def listar(cls) -> List[TipoDocumentoSchema]:
        documentos: List[TipoDocumentoSchema] = []
        try:
            filas = await TipoDocumento.listar()
            for fila in filas:
                documentos.append(TipoDocumentoSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return documentos

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await TipoDocumento.obtener(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def agregar_registro(cls, documento: TipoDocumentoPostSchema):
        try:
            return await TipoDocumento.crear(tipo_documento=documento.tipo_documento)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, documento: TipoDocumentoPutSchema):
        try:
            return await TipoDocumento.actualizar(id=str(documento.id), tipo_documento=documento.tipo_documento)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await TipoDocumento.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, documento: TipoDocumento) -> bool:
        try:
            existe = await TipoDocumento.filtarPor(tipo_documento=documento.tipo_documento)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
