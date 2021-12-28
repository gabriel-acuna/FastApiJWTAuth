from typing import List
from app.schemas.dath.SustitutoSchema import *
from app.models.dath.modelos import SustitutoPersonal
import logging


class ServicioSustituto():

    @classmethod
    async def listar_por_persona(cls, id_persona: str) -> List[SustitutoSchema]:
        sustitutos: List[SustitutoSchema] = []
        try:
            filas = await SustitutoPersonal.filtarPor(id_persona=id_persona)
            for fila in filas:
                sustitutos.append(
                    SustitutoSchema(**fila[0].__dict__)
                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return sustitutos

    @classmethod
    async def buscar_por_id(cls, id: str) -> SustitutoSchema:
        sustituto: SustitutoSchema = None
        try:
            resultado = SustitutoPersonal.obtener(id)
            if resultado:
                sustituto = SustitutoSchema(**resultado[0].__dict__)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return sustituto

    @classmethod
    async def agregar_registro(cls, sustituto: SustitutoPostSchema) -> bool:
        try:
            return await SustitutoPersonal.crear(
                id_persona=sustituto.id_persona,
                tipo_sustituto=sustituto.tipo_sustituto.name,
                apellidos=sustituto.apellidos,
                nombres=sustituto.nombres,
                numero_carnet=sustituto.numero_carnet,
                desde=sustituto.desde,
                hasta=sustituto.hasta

            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, sustituto: SustitutoPutSchema) -> bool:
        try:
            return await SustitutoPersonal.actualizar(
                id=sustituto.id,
                tipo_sustituto=sustituto.tipo_sustituto.name,
                apellidos=sustituto.apellidos,
                nombres=sustituto.nombres,
                numero_carnet=sustituto.numero_carnet,
                desde=sustituto.desde,
                hasta=sustituto.hasta
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
    
    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await SustitutoPersonal.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, sustituto: SustitutoPostSchema) -> bool:
        try:
            existe = SustitutoPersonal.filtarPor(
                id_persona = sustituto.id_persona,
                apellidos=sustituto.apellidos,
                nombres=sustituto.nombres,
                numero_carnet=sustituto.numero_carnet,
                desde=sustituto.desde,
                hasta=sustituto.hasta
            )
            return True if existe else False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)