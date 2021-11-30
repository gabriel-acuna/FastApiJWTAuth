from datetime import time
import logging
from typing import List

from sqlalchemy.sql.expression import select
from app.models.core.modelos_principales import Pais
from app.schemas.cv.CapacitacitaonSchema import *
from app.models.cv.modelos import Capacitacion, TipoCertificado as TC, TipoEvento
from app.database.conf import AsyncDatabaseSession


class ServicioCapacitacion():

    @classmethod
    async def listar(cls, id_persona: str) -> List[CapacitacionSchema]:
        capaciatciones: List[CapacitacionSchema] = []
        try:
            filas = await Capacitacion.filtarPor(id_persona=id_persona)
            if filas:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                for fila in filas:
                    pais: PaisSchema = None
                    tipo_evento: TipoEventoSchema = None
                    result = await async_db_session.execute(
                        select(Pais).where(Pais.id == fila[0].id_pais)
                    )
                    p = result.scalar_one()
                    pais = PaisSchema(**p.__dict__)
                    result = await async_db_session.execute(
                        select(TipoEvento).where(
                            TipoEvento.id == fila[0].id_tipo_evento)
                    )
                    t_evento = result.scalar_one()
                    tipo_evento = TipoEventoSchema(**t_evento.__dict__)

                    capaciatciones.append(CapacitacionSchema(
                        id=fila[0].id,
                        id_persona=fila[0].id_persona,
                        tipo_evento=tipo_evento,
                        nombre=fila[0].nombre,
                        institucion_organizadora=fila[0].institucion_organizadora,
                        funcion_evento=fila[0].funcion_evento,
                        pais=pais,
                        lugar=fila[0].lugar,
                        horas=fila[0].horas,
                        inicio=fila[0].inicio,
                        fin=fila[0].fin,
                        tipo_certificado=fila[0].tipo_certificado.value,
                        certificado=fila[0].certificado,
                        url=fila[0].url_certificado
                    )
                    )
                await async_db_session.close()
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return capaciatciones

    @classmethod
    async def buscar_por_id(cls, id: str) -> CapacitacionSchema:
        capacitacion: CapacitacionSchema = None
        try:
            resultado = await Capacitacion.obtener(id=id)
            if resultado:
                pais = await Pais.obtener(resultado[0].id_pais)
                tipo_evento = await TipoEvento.obtener(resultado[0].id_tipo_evento)

                capacitacion = CapacitacionSchema(
                    id=resultado[0].id,
                    id_persona=resultado[0].id_persona,
                    tipo_evento=TipoEventoSchema(**tipo_evento[0].__dict__),
                    nombre=resultado[0].nombre,
                    institucion_organizadora=resultado[0].institucion_organizadora,
                    funcion_evento=resultado[0].funcion_evento,
                    pais=PaisSchema(**pais[0].__dict__),
                    lugar=resultado[0].lugar,
                    horas=resultado[0].horas,
                    inicio=resultado[0].inicio,
                    fin=resultado[0].fin,
                    tipo_certificado=resultado[0].tipo_certificado.value,
                    certificado=resultado[0].certificado,
                    url=resultado[0].url_certificado
                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return capacitacion

    @classmethod
    async def agregar_registro(cls, capacitacion: CapacitacionPostSchema) -> bool:
        try:
            return await Capacitacion.crear(
                id_persona=capacitacion.id_persona,
                id_tipo_evento=capacitacion.tipo_evento,
                nombre=capacitacion.nombre,
                institucion_organizadora=capacitacion.institucion_organizadora,
                funcion_evento=capacitacion.funcion_evento,
                id_pais=capacitacion.pais,
                lugar=capacitacion.lugar,
                horas=capacitacion.horas,
                inicio=capacitacion.inicio,
                fin=capacitacion.fin,
                tipo_certificado=capacitacion.tipo_certificado,
                certificado=capacitacion.url,
                url_certificado=capacitacion.url
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, id: str, capacitacion: CapacitacionPutSchema) -> bool:
        try:

            return await Capacitacion.actualizar(
                id=id,
                id_tipo_evento=capacitacion.tipo_evento,
                nombre=capacitacion.nombre,
                institucion_organizadora=capacitacion.institucion_organizadora,
                funcion_evento=capacitacion.funcion_evento,
                id_pais=capacitacion.pais,
                lugar=capacitacion.lugar,
                horas=capacitacion.horas,
                inicio=capacitacion.inicio,
                fin=capacitacion.fin,
                tipo_certificado=capacitacion.tipo_certificado,
                certificado=capacitacion.url,
                url_certificado=capacitacion.url
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await Capacitacion.eliminar(id=id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
