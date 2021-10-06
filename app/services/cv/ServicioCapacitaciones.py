import logging
from typing import List
from app.schemas.cv.CapacitacitaonSchema import *
from app.models.cv.modelos import Capacitacion, TipoCertificado as TC

class ServicioCapacitacion():
    
    @classmethod
    async def listar(cls, id_persona: str) -> List[CapacitacionSchema]:
        capaciatciones: List[CapacitacionSchema] = []
        try:
            filas = await Capacitacion.filtarPor(id_persona=id_persona)
            if filas:
                for fila in filas:
                    tp: TipoCertificado = TipoCertificado.ASISTENCIA
                    if fila[0].tipo_certificado.name == 'APROBACION':
                        tp = TipoCertificado.APROBACION
                    capaciatciones.append(CapacitacionSchema(
                        id = fila[0].id,
                        id_persona = fila[0].id_persona,
                        tipo_evento = fila[0].tipo_evento,
                        institucion_organizadora = fila[0].institucion_organizadora,
                        lugar = fila[0].lugar,
                        horas = fila[0].horas,
                        inicio = fila[0].inicio,
                        fin = fila[0].fin,
                        tipo_certificado =  tp,
                        url = fila[0].url_certificado
                    ) 
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return capaciatciones

    @classmethod
    async def buscar_por_id(cls, id:str) -> CapacitacionSchema:
        capacitacion: CapacitacionSchema = None
        try:
            resultado = await Capacitacion.obtener(id=id)
            if resultado:
                tipo_certificado: TipoCertificado = TipoCertificado.ASISTENCIA
                if resultado[0].tipo_certificado.name == 'APROBACION':
                    tipo_certificado = TipoCertificado.APROBACION
                capacitacion = CapacitacionSchema(
                    id = resultado[0].id,
                    id_persona = resultado[0].id_persona,
                    tipo_evento = resultado[0].tipo_evento,
                    institucion_organizadora = resultado[0].institucion_organizadora,
                    lugar = resultado[0].lugar,
                    horas = resultado[0].horas,
                    inicio = resultado[0].inicio,
                    fin = resultado[0].fin,
                    tipo_certificado = tipo_certificado,
                    url = resultado[0].url_certificado
                )   
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return capacitacion

    @classmethod
    async def agregar_registro(cls, capacitacion: CapacitacionPostSchema) -> bool:
        try:
            tipo_cert: TC = TC.ASISTENCIA
            if  capacitacion.tipo_certificado.name == 'APROBACION':
                tipo_cert = TC.APROBACION
            return await Capacitacion.crear(
                id_persona = capacitacion.id_persona,
                tipo_evento = capacitacion.tipo_evento,
                institucion_organizadora = capacitacion.institucion_organizadora,
                lugar = capacitacion.lugar,
                horas = capacitacion.horas,
                inicio = capacitacion.inicio,
                fin = capacitacion.fin,
                tipo_certificado = tipo_cert,
                url_certificado = capacitacion.url
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls,id:str, capacitacion: CapacitacionPutSchema) -> bool:
        try:
            tipo_cert: TC = TC.ASISTENCIA
            if  capacitacion.tipo_certificado.name == 'APROBACION':
                tipo_cert = TC.APROBACION
            return await Capacitacion.actualizar(
                id=id,
                tipo_evento = capacitacion.tipo_evento,
                institucion_organizadora = capacitacion.institucion_organizadora,
                lugar = capacitacion.lugar,
                horas = capacitacion.horas,
                inicio = capacitacion.inicio,
                fin = capacitacion.fin,
                tipo_certificado = tipo_cert,
                url_certificado = capacitacion.url
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await Capacitacion.eliminar(id=id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
