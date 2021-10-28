from app.schemas.cv.ComprensionIdiomaSchema import *
from app.models.cv.modelos import ComprensionIdioma
from typing import List
import logging


class ServicioComprensionIdioma():

    @classmethod
    async def listar(cls, id_persona: str) -> List[ComprensionIdiomaSchema]:
        idiomas: List[ComprensionIdiomaSchema] = []

        try:
            filas = await ComprensionIdioma.filtarPor(id_persona=id_persona)
            for fila in filas:
                idiomas.append(ComprensionIdiomaSchema(
                    id = fila[0].id,
                    id_persona = fila[0].id_persona,
                    idioma = fila[0].idioma,
                    lugar_estudio = fila[0].lugar_estudio,
                    nivel_comprension = NivelComprension[fila[0].nivel_comprension.value]
                ))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return idiomas

    @classmethod
    async def buscar_por_id(cls, id: str) -> ComprensionIdiomaSchema:
        idioma: ComprensionIdiomaSchema = None

        try:
            respuesta = await ComprensionIdioma.obtener(id=id)
            if respuesta:
                idioma = ComprensionIdiomaSchema(
                    id = respuesta[0].id,
                    id_persona = respuesta[0].id_persona,
                    idioma = respuesta[0].idioma,
                    lugar_estudio = respuesta[0].lugar_estudio,
                    nivel_comprension = NivelComprension[respuesta[0].nivel_comprension.value]
                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return idioma

    @classmethod
    async def agregar_registro(cls, idioma: ComprensionIdiomaPostSchema):

        try:
            return await ComprensionIdioma.crear(
                id_persona=idioma.id_persona,
                idioma=idioma.idioma,
                lugar_estudio=idioma.lugar_estudio,
                nivel_comprension=idioma.nivel_comprension

            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, idioma: ComprensionIdiomaPutSchema):
        try:
            return await ComprensionIdioma.actualizar(
                id=idioma.id,
                idioma=idioma.idioma,
                lugar_estudio=idioma.lugar_estudio,
                nivel_comprension=idioma.nivel_comprension
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await ComprensionIdioma.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, merito: ComprensionIdiomaPostSchema) -> bool:
        try:
            existe = await ComprensionIdioma.filtarPor(
                id_persona=merito.id_persona,
                idioma=merito.idioma
            )
            if existe:
                return True
            return False

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
