from typing import List

from sqlalchemy.sql.expression import select
from app.models.dath.modelos import EstadoSumario, InformacionPersonal, RegimenDisciplinario, RegimenLaboral, ModalidadContractual, Sancion
from app.schemas.dath.RegimenDisciplinarioSchema import *
from app.database.conf import AsyncDatabaseSession
import logging


class ServicioRegimenDisciplinario():

    @classmethod
    async def listar_por_anio(cls, anio: int) -> List[RegimenDisciplinarioSchema]:
        sanciones: List[RegimenDisciplinarioSchema] = []
        try:
            filas = await RegimenDisciplinario.filtarPor(anio_sancion=anio)
            if filas:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                for fila in filas:
                    registro: RegimenDisciplinario = fila[0]
                    result = await async_db_session.execute(
                        select(InformacionPersonal.tipo_identificacion, InformacionPersonal.identificacion, InformacionPersonal.primer_nombre, InformacionPersonal.segundo_nombre,
                               InformacionPersonal.primer_apellido, InformacionPersonal.segundo_apellido
                               ).where(InformacionPersonal.identificacion == registro.id_persona)

                    )
                    persona = result.all()
                    result = await async_db_session.execute(
                        select(RegimenLaboral).where(
                            RegimenLaboral.id == registro.id_regimen)
                    )
                    regimen = result.scalar_one()
                    result = await async_db_session.execute(
                        select(ModalidadContractual).where(
                            ModalidadContractual.id == registro.id_modalidad)
                    )
                    modalidad = result.scalar_one()
                    result = await async_db_session.execute(
                        select(Sancion).where(
                            Sancion.id == registro.id_sancion)
                    )
                    sancion = result.scalar_one()
                    result = await async_db_session.execute(
                        select(EstadoSumario).where(
                            EstadoSumario.id == registro.id_estado_sumario)
                    )
                    estado = result.scalar_one()
                    sanciones.append(
                        RegimenDisciplinarioSchema(
                            id=registro.id,
                            anio_sancion=registro.anio_sancion,
                            mes_sancion=registro.mes_sancion.value,
                            persona=InformacionPersonalBasicaSchema(
                                tipo_identificacion=persona[0][0].value,
                                identificacion=persona[0][1],
                                primer_nombre=persona[0][2],
                                segundo_nombre=persona[0][3],
                                primer_apellido=persona[0][4],
                                segundo_apellido=persona[0][5],
                            ),
                            regimen_laboral=RegimenLaboralSchema(
                                **regimen.__dict__),
                            modalidad_contractual=ModalidadContractualSchema(
                                **modalidad.__dict__),
                            tipo_falta=registro.tipo_falta.value,
                            sancion=SancionSchema(**sancion.__dict__),
                            aplica_sumario=registro.aplica_sumario,
                            estado_sumario=EstadoSumarioSchema(
                                **estado.__dict__),
                            numero_sentencia=registro.numero_sentencia
                        )
                    )
                await async_db_session.close()
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return sanciones

    @classmethod
    async def listar_por_anio_mes(cls, anio: int, mes: str) -> List[RegimenDisciplinarioSchema]:
        sanciones: List[RegimenDisciplinarioSchema] = []
        try:
            filas = await RegimenDisciplinario.filtarPor(anio_sancion=anio, mes_sancion=mes)
            if filas:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                for fila in filas:
                    registro: RegimenDisciplinario = fila[0]
                    result = await async_db_session.execute(
                        select(InformacionPersonal.tipo_identificacion, InformacionPersonal.identificacion, InformacionPersonal.primer_nombre, InformacionPersonal.segundo_nombre,
                               InformacionPersonal.primer_apellido, InformacionPersonal.segundo_apellido
                               ).where(InformacionPersonal.identificacion == registro.id_persona)

                    )
                    persona = result.all()
                    result = await async_db_session.execute(
                        select(RegimenLaboral).where(
                            RegimenLaboral.id == registro.id_regimen)
                    )
                    regimen = result.scalar_one()
                    result = await async_db_session.execute(
                        select(ModalidadContractual).where(
                            ModalidadContractual.id == registro.id_modalidad)
                    )
                    modalidad = result.scalar_one()
                    result = await async_db_session.execute(
                        select(Sancion).where(
                            Sancion.id == registro.id_sancion)
                    )
                    sancion = result.scalar_one()
                    result = await async_db_session.execute(
                        select(EstadoSumario).where(
                            EstadoSumario.id == registro.id_estado_sumario)
                    )
                    estado = result.scalar_one()
                    sanciones.append(
                        RegimenDisciplinarioSchema(
                            id=registro.id,
                            anio_sancion=registro.anio_sancion,
                            mes_sancion=registro.mes_sancion.value,
                            persona=InformacionPersonalBasicaSchema(
                                tipo_identificacion=persona[0][0].value,
                                identificacion=persona[0][1],
                                primer_nombre=persona[0][2],
                                segundo_nombre=persona[0][3],
                                primer_apellido=persona[0][4],
                                segundo_apellido=persona[0][5],
                            ),
                            regimen_laboral=RegimenLaboralSchema(
                                **regimen.__dict__),
                            modalidad_contractual=ModalidadContractualSchema(
                                **modalidad.__dict__),
                            tipo_falta=registro.tipo_falta.value,
                            sancion=SancionSchema(**sancion.__dict__),
                            aplica_sumario=registro.aplica_sumario,
                            estado_sumario=EstadoSumarioSchema(
                                **estado.__dict__),
                            numero_sentencia=registro.numero_sentencia
                        )
                    )
                await async_db_session.close()
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return sanciones

    @classmethod
    async def listar_por_persona(cls, id_persona: str) -> List[RegimenDisciplinarioSchema]:
        sanciones: List[RegimenDisciplinarioSchema] = []
        try:
            filas = await RegimenDisciplinario.filtarPor(id_persona=id_persona)
            if filas:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                for fila in filas:
                    registro: RegimenDisciplinario = fila[0]
                    result = await async_db_session.execute(
                        select(InformacionPersonal.tipo_identificacion, InformacionPersonal.identificacion, InformacionPersonal.primer_nombre, InformacionPersonal.segundo_nombre,
                               InformacionPersonal.primer_apellido, InformacionPersonal.segundo_apellido
                               ).where(InformacionPersonal.identificacion == registro.id_persona)

                    )
                    persona = result.all()
                    result = await async_db_session.execute(
                        select(RegimenLaboral).where(
                            RegimenLaboral.id == registro.id_regimen)
                    )
                    regimen = result.scalar_one()
                    result = await async_db_session.execute(
                        select(ModalidadContractual).where(
                            ModalidadContractual.id == registro.id_modalidad)
                    )
                    modalidad = result.scalar_one()
                    result = await async_db_session.execute(
                        select(Sancion).where(
                            Sancion.id == registro.id_sancion)
                    )
                    sancion = result.scalar_one()
                    result = await async_db_session.execute(
                        select(EstadoSumario).where(
                            EstadoSumario.id == registro.id_estado_sumario)
                    )
                    estado = result.scalar_one()
                    sanciones.append(
                        RegimenDisciplinarioSchema(
                            id=registro.id,
                            anio_sancion=registro.anio_sancion,
                            mes_sancion=registro.mes_sancion.value,
                            persona=InformacionPersonalBasicaSchema(
                                tipo_identificacion=persona[0][0].value,
                                identificacion=persona[0][1],
                                primer_nombre=persona[0][2],
                                segundo_nombre=persona[0][3],
                                primer_apellido=persona[0][4],
                                segundo_apellido=persona[0][5],
                            ),
                            regimen_laboral=RegimenLaboralSchema(
                                **regimen.__dict__),
                            modalidad_contractual=ModalidadContractualSchema(
                                **modalidad.__dict__),
                            tipo_falta=registro.tipo_falta.value,
                            sancion=SancionSchema(**sancion.__dict__),
                            aplica_sumario=registro.aplica_sumario,
                            estado_sumario=EstadoSumarioSchema(
                                **estado.__dict__),
                            numero_sentencia=registro.numero_sentencia
                        )
                    )
                await async_db_session.close()
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return sanciones

    @classmethod
    async def buscar_por_id(cls, id: str) -> RegimenDisciplinarioSchema:
        regimen: RegimenDisciplinarioSchema = None
        try:
            respuesta = await RegimenDisciplinario.obtener(id)
            if respuesta:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                result = await async_db_session.execute(
                    select(InformacionPersonal.tipo_identificacion, InformacionPersonal.identificacion, InformacionPersonal.primer_nombre, InformacionPersonal.segundo_nombre,
                           InformacionPersonal.primer_apellido, InformacionPersonal.segundo_apellido
                           ).where(InformacionPersonal.identificacion == respuesta[0].id_persona)

                )
                persona = result.all()
                result = await async_db_session.execute(
                    select(RegimenLaboral).where(
                        RegimenLaboral.id == respuesta[0].id_regimen)
                )
                regimen_laboral = result.scalar_one()
                result = await async_db_session.execute(
                    select(ModalidadContractual).where(
                        ModalidadContractual.id == respuesta[0].id_modalidad)
                )
                modalidad = result.scalar_one()
                result = await async_db_session.execute(
                    select(Sancion).where(
                        Sancion.id == respuesta[0].id_sancion)
                )
                sancion = result.scalar_one()
                result = await async_db_session.execute(
                    select(EstadoSumario).where(
                        EstadoSumario.id == respuesta[0].id_estado_sumario)
                )
                estado = result.scalar_one()

                regimen = RegimenDisciplinarioSchema(
                    id=respuesta[0].id,
                    anio_sancion=respuesta[0].anio_sancion,
                    mes_sancion=respuesta[0].mes_sancion.value,
                    persona=InformacionPersonalBasicaSchema(
                        tipo_identificacion=persona[0][0].value,
                        identificacion=persona[0][1],
                        primer_nombre=persona[0][2],
                        segundo_nombre=persona[0][3],
                        primer_apellido=persona[0][4],
                        segundo_apellido=persona[0][5],
                    ),
                    regimen_laboral=RegimenLaboralSchema(
                        **regimen_laboral.__dict__),
                    modalidad_contractual=ModalidadContractualSchema(
                        **modalidad.__dict__),
                    tipo_falta=respuesta[0].tipo_falta.value,
                    sancion=SancionSchema(**sancion.__dict__),
                    aplica_sumario=respuesta[0].aplica_sumario,
                    estado_sumario=EstadoSumarioSchema(
                        **estado.__dict__),
                    numero_sentencia=respuesta[0].numero_sentencia
                )
                await async_db_session.close()
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return regimen

    @ classmethod
    async def agregar_registro(cls, sancion: RegimenDisciplinarioPostSchema) -> bool:
        try:
            return await RegimenDisciplinario.crear(
                anio_sancion=sancion.anio_sancion,
                mes_sancion=sancion.mes_sancion,
                id_persona=sancion.persona,
                id_regimen=sancion.regimen_laboral,
                id_modalidad=sancion.modalidad_contractual,
                tipo_falta=sancion.tipo_falta,
                id_sancion=sancion.sancion,
                aplica_sumario=sancion.aplica_sumario,
                id_estado_sumario=sancion.estado_sumario,
                numero_sentencia=sancion.numero_sentencia)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)


    @ classmethod
    async def actualizar_registro(cls, sancion: RegimenDisciplinarioPutSchema) -> bool:
        try:
            return await RegimenDisciplinario.actualizar(
                id=sancion.id,
                anio_sancion=sancion.anio_sancion,
                mes_sancion=sancion.mes_sancion,
                id_persona=sancion.persona,
                id_regimen=sancion.regimen_laboral,
                id_modalidad=sancion.modalidad_contractual,
                tipo_falta=sancion.tipo_falta,
                id_sancion=sancion.sancion,
                aplica_sumario=sancion.aplica_sumario,
                id_estado_sumario = sancion.estado_sumario,
                numero_sentencia=sancion.numero_sentencia)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @ classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await RegimenDisciplinario.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @ classmethod
    async def existe(cls, sancion: RegimenDisciplinarioPostSchema) -> bool:
        try:
            existe = await RegimenDisciplinario.filtarPor(
                anio_sancion=sancion.anio_sancion,
                mes_sancion=sancion.mes_sancion,
                id_persona=sancion.persona,
                id_sancion=sancion.sancion
            )
            return True if existe else False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
