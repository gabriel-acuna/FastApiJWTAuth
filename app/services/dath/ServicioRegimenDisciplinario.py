from typing import List

from sqlalchemy.sql.expression import select
from app.models.dath.modelos import EstadoSumario, InformacionPersonal, RegimenDisciplinario, RegimenLaboral, ModalidadContractual, Sancion
from app.schemas.dath.RegimenDisciplinarioSchema import *
from app.database.conf import AsyncDatabaseSession
import logging

class ServicioRegimenDisciplinario():

    @classmethod
    async def listar_por_anio(cls, anio:int)->List[RegimenDisciplinarioSchema]:
        sanciones:List[RegimenDisciplinarioSchema] = []
        try:
            filas = await RegimenDisciplinario.filtarPor(anio_sancion=int)
            if filas:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                for fila in filas:
                    registro: RegimenDisciplinario = fila[0]
                    result = await async_db_session.execute(
                        select(InformacionPersonal.identificacion,InformacionPersonal.primer_nombre, InformacionPersonal.segundo_nombre,
                            InformacionPersonal.primer_apellido, InformacionPersonal.segundo_apellido
                        ).where(InformacionPersonal.identificacion==registro.id_persona)
                    
                    )
                    persona = result.all()
                    result = await async_db_session.execute(
                        select(RegimenLaboral).where(RegimenLaboral.id == registro.id_regimen)
                    )
                    regimen = result.scalar_one()
                    result = await async_db_session.execute(
                        select(ModalidadContractual).where(ModalidadContractual.id == registro.id_modalidad)
                    )
                    modalidad = result.scalar_one()
                    result = await async_db_session.execute(
                        select(Sancion).where(Sancion.id == registro.id_sancion)
                    )
                    sancion = result.scalar_one()
                    result = await async_db_session.execute(
                        select(EstadoSumario).where(EstadoSumario.id == registro.id_estado_sumario)
                    )
                    estado = result.scalar_one()
                    sanciones.append(
                        RegimenDisciplinarioSchema(
                            id=registro.id,
                            anio_sancion = registro.anio_sancion,
                            mes = registro.MES,
                            persona = {
                                'identificacion': persona[0][0],
                                'nombres': f'{persona[0][1]} {persona[0][2]}',
                                'apellidos': f'{persona[0][3]} {persona[0][4]}'
                            },
                            regimen_laboral = RegimenLaboralSchema(**regimen.__dict__),
                            modalidad_contractual = ModalidadContractualSchema(**modalidad.__dict__),
                            tipo_falta = registro.tipo_falta,
                            sancion = SancionSchema(**sancion.__dict__),
                            aplica_sumario = registro.aplica_sumario,
                            estado_sumario = EstadoSumarioSchema(**estado.__dict__),
                            numero_sentencia = registro.numero_sentencia
                        )
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
    

        return sanciones


    @classmethod
    async def listar_por_anio_mes(cls, anio:int, mes: str) ->List[RegimenDisciplinarioSchema]:
        sanciones:List[RegimenDisciplinarioSchema] = []
        try:
            filas = await RegimenDisciplinario.filtarPor(anio_sancion=int, mes_sanncion=mes)
            if filas:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                for fila in filas:
                    registro: RegimenDisciplinario = fila[0]
                    result = await async_db_session.execute(
                        select(InformacionPersonal.identificacion,InformacionPersonal.primer_nombre, InformacionPersonal.segundo_nombre,
                            InformacionPersonal.primer_apellido, InformacionPersonal.segundo_apellido
                        ).where(InformacionPersonal.identificacion==registro.id_persona)
                    
                    )
                    persona = result.all()
                    result = await async_db_session.execute(
                        select(RegimenLaboral).where(RegimenLaboral.id == registro.id_regimen)
                    )
                    regimen = result.scalar_one()
                    result = await async_db_session.execute(
                        select(ModalidadContractual).where(ModalidadContractual.id == registro.id_modalidad)
                    )
                    modalidad = result.scalar_one()
                    result = await async_db_session.execute(
                        select(Sancion).where(Sancion.id == registro.id_sancion)
                    )
                    sancion = result.scalar_one()
                    result = await async_db_session.execute(
                        select(EstadoSumario).where(EstadoSumario.id == registro.id_estado_sumario)
                    )
                    estado = result.scalar_one()
                    sanciones.append(
                        RegimenDisciplinarioSchema(
                            id=registro.id,
                            anio_sancion = registro.anio_sancion,
                            persona = {
                                'identificacion': persona[0][0],
                                'nombres': f'{persona[0][1]} {persona[0][2]}',
                                'apellidos': f'{persona[0][3]} {persona[0][4]}'
                            },
                            regimen_laboral = RegimenLaboralSchema(**regimen.__dict__),
                            modalidad_contractual = ModalidadContractualSchema(**modalidad.__dict__),
                            tipo_falta = registro.tipo_falta,
                            sancion = SancionSchema(**sancion.__dict__),
                            aplica_sumario = registro.aplica_sumario,
                            estado_sumario = EstadoSumarioSchema(**estado.__dict__),
                            numero_sentencia = registro.numero_sentencia
                        )
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
    

        return sanciones

    @classmethod
    async def listar_por_persona(cls, id_persona:str) ->List[RegimenDisciplinarioSchema]:
        sanciones:List[RegimenDisciplinarioSchema] = []
        try:
            filas = await RegimenDisciplinario.filtarPor(id_persona=id_persona)
            if filas:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                for fila in filas:
                    registro: RegimenDisciplinario = fila[0]
                    result = await async_db_session.execute(
                        select(InformacionPersonal.identificacion,InformacionPersonal.primer_nombre, InformacionPersonal.segundo_nombre,
                            InformacionPersonal.primer_apellido, InformacionPersonal.segundo_apellido
                        ).where(InformacionPersonal.identificacion==registro.id_persona)
                    
                    )
                    persona = result.all()
                    result = await async_db_session.execute(
                        select(RegimenLaboral).where(RegimenLaboral.id == registro.id_regimen)
                    )
                    regimen = result.scalar_one()
                    result = await async_db_session.execute(
                        select(ModalidadContractual).where(ModalidadContractual.id == registro.id_modalidad)
                    )
                    modalidad = result.scalar_one()
                    result = await async_db_session.execute(
                        select(Sancion).where(Sancion.id == registro.id_sancion)
                    )
                    sancion = result.scalar_one()
                    result = await async_db_session.execute(
                        select(EstadoSumario).where(EstadoSumario.id == registro.id_estado_sumario)
                    )
                    estado = result.scalar_one()
                    sanciones.append(
                        RegimenDisciplinarioSchema(
                            id=registro.id,
                            anio_sancion = registro.anio_sancion,
                            persona = {
                                'identificacion': persona[0][0],
                                'nombres': f'{persona[0][1]} {persona[0][2]}',
                                'apellidos': f'{persona[0][3]} {persona[0][4]}'
                            },
                            regimen_laboral = RegimenLaboralSchema(**regimen.__dict__),
                            modalidad_contractual = ModalidadContractualSchema(**modalidad.__dict__),
                            tipo_falta = registro.tipo_falta,
                            sancion = SancionSchema(**sancion.__dict__),
                            aplica_sumario = registro.aplica_sumario,
                            estado_sumario = EstadoSumarioSchema(**estado.__dict__),
                            numero_sentencia = registro.numero_sentencia
                        )
                    )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
    

        return sanciones