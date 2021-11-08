from typing import List
from app.models.core.modelos_principales import CampoEducativoAmplio
from app.schemas.core.CampoEducativoSchema import CampoEducativoAmplioPostSchema, CampoEducativoAmplioPutSchema, CampoEducativoAmplioSchema
import logging

class ServicioCampoEducativoAmplio():

    @classmethod
    async def listar(cls) -> List[CampoEducativoAmplioSchema] :
        campos: List[CampoEducativoAmplioSchema] = []
        try:
            filas = await CampoEducativoAmplio.listar()
            if filas:
                for fila in filas:
                    campo: CampoEducativoAmplio = fila[0]
                    campos.append(
                        CampoEducativoAmplioSchema(
                            id = campo.id,
                            codigo = campo.codigo,
                            descripcion = campo.descripcion
                        )
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return campos

    @classmethod
    async def  buscar_por_id(cls, id:str) -> CampoEducativoAmplioSchema:
        campo: CampoEducativoAmplioSchema = None
        try:
            resultado = await CampoEducativoAmplio.obtener(id)
            if resultado:
                campo = CampoEducativoAmplioSchema(
                            id = resultado[0].id,
                            codigo = resultado[0].codigo,
                            descripcion = resultado[0].descripcion
                        )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return campo

    @classmethod
    async def agregar_registro(cls, campo: CampoEducativoAmplioPostSchema):
        try:
            return await CampoEducativoAmplio.crear(
                codigo=campo.codigo,
                descripcion = campo.descripcion
                
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, campo: CampoEducativoAmplioPutSchema):
        try:
            return await CampoEducativoAmplio.actualizar(
                id = campo.id,
                codigo=campo.codigo,
                descripcion = campo.descripcion
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await CampoEducativoAmplio.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, campo: CampoEducativoAmplioPostSchema) -> bool:
        try:
            existe = await CampoEducativoAmplio.filtarPor(
                codigo=campo.codigo,
                descripcion = campo.descripcion
            )
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
