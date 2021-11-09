from typing import List
from app.models.core.modelos_principales import CampoEducativoDetallado, CampoEducativoEspecifico
from app.schemas.core.CampoEducativoSchema import CampoEducativoDetalladoSchema, CampoEducativoEspecificoPostSchema, CampoEducativoEspecificoPutSchema, CampoEducativoEspecificoSchema
import logging


class ServicioCampoEducativoEspecifico():

    @classmethod
    async def listar(cls) -> List[CampoEducativoEspecificoSchema]:
        campos: List[CampoEducativoEspecificoSchema] = []
        try:
            filas = await CampoEducativoEspecifico.listar()
            if filas:
                for fila in filas:
                    campo: CampoEducativoEspecifico = fila[0]
                    campos.append(
                        CampoEducativoEspecificoSchema(
                            id=campo.id,
                            campo_amplio=campo.id_campo_amplio,
                            codigo=campo.codigo,
                            descripcion=campo.descripcion
                        )
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return campos

    @classmethod
    async def buscar_por_id(cls, id: str) -> CampoEducativoEspecificoSchema:
        campo: CampoEducativoEspecificoSchema = None
        try:
            resultado = await CampoEducativoEspecifico.obtener(id)
            if resultado:
                campo = CampoEducativoEspecificoSchema(
                    id=resultado[0].id,
                    campo_amplio=resultado[0].id_campo_amplio,
                    codigo=resultado[0].codigo,
                    descripcion=resultado[0].descripcion
                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return campo

    @classmethod
    async def listar_campos_detallados(cls, id: str) -> List[CampoEducativoDetalladoSchema]:
        campos: CampoEducativoDetalladoSchema = []
        try:
            filas = await CampoEducativoDetallado.filtarPor(id_campo_especifico=id)
            if filas:
                for fila in filas:
                    campos.append(CampoEducativoDetalladoSchema(
                        id=fila[0].id,
                        campo_especifico=fila[0].id_campo_especifico,
                        codigo=fila[0].codigo,
                        descripcion=fila[0].descripcion
                    ))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return campos

    @classmethod
    async def agregar_registro(cls, campo: CampoEducativoEspecificoPostSchema):
        try:
            return await CampoEducativoEspecifico.crear(
                codigo=campo.codigo,
                id_campo_amplio=campo.campo_amplio,
                descripcion=campo.descripcion

            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, campo: CampoEducativoEspecificoPutSchema):
        try:
            return await CampoEducativoEspecifico.actualizar(
                id=campo.id,
                codigo=campo.codigo,
                id_campo_amplio=campo.campo_amplio,
                descripcion=campo.descripcion

            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await CampoEducativoEspecifico.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, campo: CampoEducativoEspecificoPostSchema) -> bool:
        try:
            existe = await CampoEducativoEspecifico.filtarPor(
                codigo=campo.codigo,
                id_campo_amplio=campo.campo_amplio,
                descripcion=campo.descripcion
            )
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
