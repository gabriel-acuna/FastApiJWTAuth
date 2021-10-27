from typing import List
from app.models.core.modelos_principales import CampoEducativoDetallado, CampoEducativoEspecifico
from app.schemas.core.CampoEducativoSchema import CampoEducativoDetalladoPostSchema, CampoEducativoDetalladoPutSchema, CampoEducativoDetalladoSchema
import logging
class ServicioCampoEducativoDetallado():

    @classmethod
    async def listar(cls) -> List[CampoEducativoDetalladoSchema] :
        campos: List[CampoEducativoDetalladoSchema] = []
        try:
            filas = await CampoEducativoDetallado.listar()
            if filas:
                for fila in filas:
                    campo: CampoEducativoDetallado = fila[0]
                    campos.append(
                        CampoEducativoDetalladoSchema(
                            id = campo.id,
                            campo_especifico = campo.id_campo_especifico,
                            codigo = campo.codigo,
                            descripcion = campo.descripcion
                        )
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return campos

    @classmethod
    async def  buscar_por_id(cls, id:str) -> CampoEducativoDetalladoSchema:
        campo: CampoEducativoDetalladoSchema = None
        try:
            resultado = await CampoEducativoDetallado.obtener(id)
            if resultado:
                campo = CampoEducativoDetalladoSchema(
                            id = resultado[0].id,
                            campo_especifico = resultado[0].id_campo_especifico,
                            codigo = resultado[0].codigo,
                            descripcion = resultado[0].descripcion
                        )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return campo

    @classmethod
    async def agregar_registro(cls, campo: CampoEducativoDetalladoPostSchema):
        try:
            return await CampoEducativoDetallado.crear(
                codigo=campo.codigo,
                id_campo_especifico = campo.campo_especifico,
                descripcion = campo.descripcion
                
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, campo: CampoEducativoDetalladoPutSchema):
        try:
            return await CampoEducativoDetallado.actualizar(
                id = campo.id,
                codigo=campo.codigo,
                id_campo_especifico = campo.campo_especifico,
                descripcion = campo.descripcion
                
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await CampoEducativoDetallado.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, campo: CampoEducativoDetalladoPostSchema) -> bool:
        try:
            existe = await CampoEducativoDetallado.filtarPor(
                codigo=campo.codigo,
                id_campo_especifico = campo.campo_especifico,
                descripcion = campo.descripcion
            )
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
