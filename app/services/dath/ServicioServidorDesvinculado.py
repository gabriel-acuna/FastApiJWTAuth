from typing import List

from sqlalchemy.sql.expression import select
from app.models.core.modelos_principales import Canton, Provincia

from app.schemas.dath.DireccionSchema import DireccionSchema, ProvinciaSchema, CantonSchema
from app.schemas.dath.ServidorDesvinculadoSchema import *
from app.models.dath.modelos import DireccionDomicilio, ExpedienteLaboral, ModalidadContractual, MotivoDesvinculacion, RegimenLaboral, ServidorDesvinculado, InformacionPersonal
import logging
from app.database.conf import AsyncDatabaseSession


class ServicioServidorDesvinculado():

    @classmethod
    async def listar_por_año(cls, año: int) -> List[ServidorDesvinculadoSchema]:
        servidores_desvinculados: List[ServidorDesvinculadoSchema] = []
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            res = await async_db_session.execute(
                select(ServidorDesvinculado).where(
                    ServidorDesvinculado.fecha_salida.year == año)
            )
            filas = res.all()
            for fila in filas:
                result = await async_db_session.execute(
                    select(InformacionPersonal.identificacion, InformacionPersonal.primer_nombre, InformacionPersonal.segundo_nombre,
                           InformacionPersonal.primer_apellido, InformacionPersonal.segundo_apellido
                           ).where(InformacionPersonal.identificacion == fila[0].id_persona)

                )
                persona = result.all()
                res = await async_db_session.execute(
                    select(DireccionDomicilio).where(
                        DireccionDomicilio.id_persona == fila[0].id_persona)
                )
                direccion = res.scalar_one()
                res = await async_db_session.executa(
                    select(Provincia).where(
                        Provincia.id == direccion.id_provincia)
                )
                provincia = res.scalar_one()

                res = await async_db_session.execute(
                    select(Canton).where(
                        Canton.id == direccion.id_canton
                    )
                )
                canton = res.scalar_one()
                res = await async_db_session.execute(
                    select(ExpedienteLaboral.registrado_en).where(
                        ExpedienteLaboral.id_persona == fila[0].id_persona)
                )
                ingreso = res.all()
                res = await async_db_session.execute(
                    select(MotivoDesvinculacion).where(
                        MotivoDesvinculacion.id == fila[0].id_motivo_desvinculacion,
                    )
                )
                motivo_desvinculacion = res.scalar_one()
                res = await async_db_session.execute(
                    select(ModalidadContractual).where(
                        ModalidadContractual.id == fila[0].id_modalidad
                    )
                )
                modalidad = res.scalar_one()
                res = await async_db_session.execute(
                    select(RegimenLaboral).where(
                        RegimenLaboral.id == fila[0].id_regimen)
                )
                regimen = res.scalar_one()

                servidores_desvinculados.append(
                    ServidorDesvinculadoSchema(
                        id=fila[0].id,
                        institucion=fila[0].institucion,
                        ruc=fila[0].ruc,
                        persona=InformacionPersonalResumenSchema(
                            tipo_identificacion=persona[0][0],
                            identificacion=persona[0][1],
                            primer_nombre=persona[0][2],
                            segundo_nombre=persona[0][3],
                            primer_apellido=persona[0][4],
                            segundo_apellido=persona[0][5],
                            direccion_domicilio=DireccionSchema(
                                id=direccion.id,
                                provincia=ProvinciaSchema(
                                    **provincia.__dict__),
                                canton=CantonSchema(**canton.__dict__),
                                parroquia=direccion.parroquia,
                                calle1=direccion.calle1,
                                calle2=direccion.calle2,
                                referencia=direccion.referencia
                            ),
                            fecha_ingreso=ingreso
                        ),
                        fecha_ingreso=ingreso,
                        fecha_salida=fila[0].fecha_salida,
                        nombre_planta=fila[0].nombre_planta,
                        regimen=RegimenLaboralSchema(**regimen.__dict__),
                        modalidad=ModalidadContractualSchema(
                            **modalidad.__dict__),
                        grupo_ocupacional=fila[0].grupo_ocupacional,
                        motivo_desvinculacion=MotivoDesvinculacionSchema(
                            **motivo_desvinculacion.__dict__),
                        pago_liquidacion=fila[0].pago_liquidacion,
                        fecha_pago=fila[0].fecha_pago,
                        valor_cancelado=fila[0].valor_cancelado,
                        motivo_incumplimiento=fila[0].motivo_incumplimiento
                    )
                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()

        return servidores_desvinculados

    @classmethod
    async def listar_por_año_mes(cls, año: int, mes: int) -> List[ServidorDesvinculadoSchema]:
        servidores_desvinculados: List[ServidorDesvinculadoSchema] = []
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            res = await async_db_session.execute(
                select(ServidorDesvinculado).where(
                    ServidorDesvinculado.fecha_salida.year == año,
                    ServidorDesvinculado.fecha_salida.month == mes
                )
            )
            filas = res.all()
            for fila in filas:
                result = await async_db_session.execute(
                    select(InformacionPersonal.identificacion, InformacionPersonal.primer_nombre, InformacionPersonal.segundo_nombre,
                           InformacionPersonal.primer_apellido, InformacionPersonal.segundo_apellido
                           ).where(InformacionPersonal.identificacion == fila[0].id_persona)

                )
                persona = result.all()
                res = await async_db_session.execute(
                    select(DireccionDomicilio).where(
                        DireccionDomicilio.id_persona == fila[0].id_persona)
                )
                direccion = res.scalar_one()
                res = await async_db_session.executa(
                    select(Provincia).where(
                        Provincia.id == direccion.id_provincia)
                )
                provincia = res.scalar_one()

                res = await async_db_session.execute(
                    select(Canton).where(
                        Canton.id == direccion.id_canton
                    )
                )
                canton = res.scalar_one()
                res = await async_db_session.execute(
                    select(ExpedienteLaboral.registrado_en).where(
                        ExpedienteLaboral.id_persona == fila[0].id_persona)
                )
                ingreso = res.all()
                res = await async_db_session.execute(
                    select(MotivoDesvinculacion).where(
                        MotivoDesvinculacion.id == fila[0].id_motivo_desvinculacion,
                    )
                )
                motivo_desvinculacion = res.scalar_one()
                res = await async_db_session.execute(
                    select(ModalidadContractual).where(
                        ModalidadContractual.id == fila[0].id_modalidad
                    )
                )
                modalidad = res.scalar_one()
                res = await async_db_session.execute(
                    select(RegimenLaboral).where(
                        RegimenLaboral.id == fila[0].id_regimen)
                )
                regimen = res.scalar_one()

                servidores_desvinculados.append(
                    ServidorDesvinculadoSchema(
                        id=fila[0].id,
                        institucion=fila[0].institucion,
                        ruc=fila[0].ruc,
                        persona=InformacionPersonalResumenSchema(
                            tipo_identificacion=persona[0][0],
                            identificacion=persona[0][1],
                            primer_nombre=persona[0][2],
                            segundo_nombre=persona[0][3],
                            primer_apellido=persona[0][4],
                            segundo_apellido=persona[0][5],
                            direccion_domicilio=DireccionSchema(
                                id=direccion.id,
                                provincia=ProvinciaSchema(
                                    **provincia.__dict__),
                                canton=CantonSchema(**canton.__dict__),
                                parroquia=direccion.parroquia,
                                calle1=direccion.calle1,
                                calle2=direccion.calle2,
                                referencia=direccion.referencia
                            ),
                            fecha_ingreso=ingreso
                        ),
                        fecha_ingreso=ingreso,
                        fecha_salida=fila[0].fecha_salida,
                        nombre_planta=fila[0].nombre_planta,
                        regimen=RegimenLaboralSchema(**regimen.__dict__),
                        modalidad=ModalidadContractualSchema(
                            **modalidad.__dict__),
                        grupo_ocupacional=fila[0].grupo_ocupacional,
                        motivo_desvinvulacion=MotivoDesvinculacionSchema(
                            **motivo_desvinculacion.__dict__),
                        pago_liquidacion=fila[0].pago_liquidacion,
                        fecha_pago=fila[0].fecha_pago,
                        valor_cancelado=fila[0].valor_cancelado,
                        motivo_incumplimiento=fila[0].motivo_incumplimiento
                    )
                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()

        return servidores_desvinculados

    @classmethod
    async def buscar_por_id(cls, id: str) -> ServidorDesvinculadoSchema:
        servidor_desvinculado: ServidorDesvinculado
        try:
            resultado = await ServidorDesvinculado.obtener(id)
            if resultado:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()

                result = await async_db_session.execute(
                    select(InformacionPersonal.identificacion, InformacionPersonal.primer_nombre, InformacionPersonal.segundo_nombre,
                           InformacionPersonal.primer_apellido, InformacionPersonal.segundo_apellido
                           ).where(InformacionPersonal.identificacion == resultado[0].id_persona)

                )
                persona = result.all()
                res = await async_db_session.execute(
                    select(DireccionDomicilio).where(
                        DireccionDomicilio.id_persona == resultado[0].id_persona)
                )
                direccion = res.scalar_one()
                res = await async_db_session.executa(
                    select(Provincia).where(
                        Provincia.id == direccion.id_provincia)
                )
                provincia = res.scalar_one()

                res = await async_db_session.execute(
                    select(Canton).where(
                        Canton.id == direccion.id_canton
                    )
                )
                canton = res.scalar_one()
                res = await async_db_session.execute(
                    select(ExpedienteLaboral.registrado_en).where(
                        ExpedienteLaboral.id_persona == resultado[0].id_persona)
                )
                ingreso = res.all()
                res = await async_db_session.execute(
                    select(MotivoDesvinculacion).where(
                        MotivoDesvinculacion.id == resultado[0].id_motivo_desvinculacion,
                    )
                )
                motivo_desvinculacion = res.scalar_one()
                res = await async_db_session.execute(
                    select(ModalidadContractual).where(
                        ModalidadContractual.id == resultado[0].id_modalidad
                    )
                )
                modalidad = res.scalar_one()
                res = await async_db_session.execute(
                    select(RegimenLaboral).where(
                        RegimenLaboral.id == resultado[0].id_regimen)
                )
                regimen = res.scalar_one()

                servidor_desvinculado = ServidorDesvinculadoSchema(
                    id=resultado[0].id,
                    institucion=resultado[0].institucion,
                    ruc=resultado[0].ruc,
                    persona=InformacionPersonalResumenSchema(
                        tipo_identificacion=persona[0][0],
                        identificacion=persona[0][1],
                        primer_nombre=persona[0][2],
                        segundo_nombre=persona[0][3],
                        primer_apellido=persona[0][4],
                        segundo_apellido=persona[0][5],
                        direccion_domicilio=DireccionSchema(
                            id=direccion.id,
                            provincia=ProvinciaSchema(
                                **provincia.__dict__),
                            canton=CantonSchema(**canton.__dict__),
                            parroquia=direccion.parroquia,
                            calle1=direccion.calle1,
                            calle2=direccion.calle2,
                            referencia=direccion.referencia
                        ),
                        fecha_ingreso=ingreso
                    ),
                    fecha_ingreso=ingreso,
                    fecha_salida=resultado[0].fecha_salida,
                    nombre_planta=resultado[0].nombre_planta,
                    regimen=RegimenLaboralSchema(**regimen.__dict__),
                    modalidad=ModalidadContractualSchema(
                        **modalidad.__dict__),
                    grupo_ocupacional=resultado[0].grupo_ocupacional,
                    motivo_desvinvulacion=MotivoDesvinculacionSchema(
                        **motivo_desvinculacion.__dict__),
                    pago_liquidacion=resultado[0].pago_liquidacion,
                    fecha_pago=resultado[0].fecha_pago,
                    valor_cancelado=resultado[0].valor_cancelado,
                    motivo_incumplimiento=resultado[0].motivo_incumplimiento
                )

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()

        return servidor_desvinculado

    @classmethod
    async def agregar_registro(cls, servidor_desvinculado: ServidorDesvinculadoPostSchema) -> bool:
        try:
            return await ServidorDesvinculado.crear(
                id_persona= servidor_desvinculado.persona,
                fecha_ingreso=servidor_desvinculado.fecha_ingreso,
                fecha_salida= servidor_desvinculado.fecha_salida,
                nombre_planta=servidor_desvinculado.nombre_planta,
                id_regimen=servidor_desvinculado.regimen,
                id_modalidad=servidor_desvinculado.modalidad,
                grupo_ocupacional=servidor_desvinculado.grupo_ocupacional,
                id_motivo_desvinculacion=servidor_desvinculado.motivo_desvinculacion,
                pago_liquidacion=servidor_desvinculado.pago_liquidacion,
                fecha_pago= servidor_desvinculado if servidor_desvinculado else None,
                valor_cancelado= servidor_desvinculado.valor_cancelado,
                motivo_incumplimiento=servidor_desvinculado.motivo_incumplimiento if servidor_desvinculado.motivo_incumplimiento else None
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, servidor_desvinculado: ServidorDesvinculadoPutSchema) -> bool:
        try:
            return await ServidorDesvinculado.actualizar(
                id= servidor_desvinculado.id,
                id_persona= servidor_desvinculado.persona,
                fecha_ingreso=servidor_desvinculado.fecha_ingreso,
                fecha_salida= servidor_desvinculado.fecha_salida,
                nombre_planta=servidor_desvinculado.nombre_planta,
                id_regimen=servidor_desvinculado.regimen,
                id_modalidad=servidor_desvinculado.modalidad,
                grupo_ocupacional=servidor_desvinculado.grupo_ocupacional,
                id_motivo_desvinculacion=servidor_desvinculado.motivo_desvinculacion,
                pago_liquidacion=servidor_desvinculado.pago_liquidacion,
                fecha_pago= servidor_desvinculado if servidor_desvinculado else None,
                valor_cancelado= servidor_desvinculado.valor_cancelado,
                motivo_incumplimiento=servidor_desvinculado.motivo_incumplimiento if servidor_desvinculado.motivo_incumplimiento else None
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await ServidorDesvinculado.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
    
    @classmethod
    async def existe(cls, servidor_desvinculado: ServidorDesvinculadoPostSchema) ->  bool:
        try:
            existe = await ServidorDesvinculado.filtarPor(
                id_persona  = servidor_desvinculado.persona,
                fecha_salida = servidor_desvinculado.fecha_salida
            )
            return True if existe else False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
