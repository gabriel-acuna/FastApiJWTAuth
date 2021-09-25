import logging
import typing
from typing import List
from app.models.cv.modelos import Referencia
from app.schemas.cv.ReferenciaSchema import *


class ServicioReferencia():
    

    @classmethod
    async def listar(cls, id_persona: str) -> List[ReferenciaSchema]:
        referencias: List[ReferenciaSchema] = []
        try:
            filas = await Referencia.filtarPor(id_persona=id_persona)
            if filas:
                for fila in filas:
                    referencias.append(
                        ReferenciaSchema(
                            id = fila[0].id,
                            id_persona = fila[0].id_persona,
                            referencia= TipoReferencia[fila[0].tipo_referencia.value],
                            apellidos = fila[0].apellidos,
                            nombres = fila[0].nombres,
                            direccion = fila[0].direccion,
                            correo_electronico = fila[0].correo_electronico,
                            telefono_domicilio = fila[0].telefono_domicilio,
                            telefono_movil = fila[0].telefono_movil
                        )
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return referencias

    @classmethod
    async def buscar_por_id(cls, id:str)->ReferenciaSchema:
        referencia: ReferenciaSchema = None
        try:
            ref = Referencia.obtener(
                id = id
            )
            referencia = ReferenciaSchema(
                            id = ref[0].id,
                            id_persona = ref[0].id_persona,
                            referencia= TipoReferencia[ref[0].tipo_referencia.value],
                            apellidos = ref[0].apellidos,
                            nombres = ref[0].nombres,
                            direccion = ref[0].direccion,
                            correo_electronico = ref[0].correo_electronico,
                            telefono_domicilio = ref[0].telefono_domicilio,
                            telefono_movil = ref[0].telefono_movil
                        )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return referencia


    @classmethod
    async def agregar_registro(cls, referencia: ReferenciaPostSchema) -> bool:
        try:
            return await Referencia.crear(
                id_persona = referencia.id_persona,
                referencia = referencia.referencia,
                apellidos = referencia.apellidos,
                nombres = referencia.nombres,
                direccion = referencia.direccion,
                correo_electronico = referencia.correo_electronico,
                telefono_domicilio = referencia.telefono_domicilio,
                telefono_movil = referencia.telefono_movil
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
    
    @classmethod
    async def actualizar_registro(cls, id: str, referencia: ReferenciaPutSchema) -> bool:
        try:
            return await Referencia.actualizar(
                id = id,
                referencia = referencia.referencia,
                apellidos = referencia.apellidos,
                nombres = referencia.nombres,
                direccion = referencia.direccion,
                correo_electronico = referencia.correo_electronico,
                telefono_domicilio = referencia.telefono_domicilio,
                telefono_movil = referencia.telefono_movil
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id:str)->bool:
        try:
            return await Referencia.eliminar(id=id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)