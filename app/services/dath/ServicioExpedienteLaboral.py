from typing import List, Union
from sqlalchemy.sql.expression import desc, false, select
from app.models.dath.modelos import ExpedienteLaboral, DetalleExpedienteLaboral, TipoContrato, TipoNombramiento, TipoPersonal as TP
from app.models.core.modelos_principales import TipoDocumento, RelacionIES, TipoEscalafonNombramiento, TiempoDedicacionProfesor
from app.models.core.modelos_principales import CategoriaContratoProfesor, TipoFuncionario, TipoDocenteLOES
from app.models.core.modelos_principales import CategoriaDocenteLOSEP, NivelEducativo, AreaInstitucion
from app.schemas.dath.DetalleExpedienteSchema import *
from app.schemas.dath.ExpedienteLaboralSchema import ExpedienteLaboralSchema
from app.database.conf import AsyncDatabaseSession
import logging


class ServicioExpedienteLaboral():

    @classmethod
    async def listar(cls, id_persona: str) -> ExpedienteLaboralSchema:
        expediente: ExpedienteLaboralSchema = None
        lista_expediente: List[DetalleExpedienteSchema] = []
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            result = await async_db_session.execute(
                select(ExpedienteLaboral).where(
                    ExpedienteLaboral.id_persona == id_persona
                )
            )
            expediente_laboral = result.scalar_one()

            if expediente_laboral:
                result = await async_db_session.execute(select(DetalleExpedienteLaboral).where(
                    DetalleExpedienteLaboral.id_expediente == expediente_laboral.id))
                filas = result.all()
                
                for fila in filas:
                    
                    detalle = await ServicioExpedienteLaboral.buscar_por_id_con_session(id=fila[0].id, async_db_session=async_db_session)
                    if detalle:
                        lista_expediente.append(detalle)
                expediente = ExpedienteLaboralSchema(
                    id=expediente_laboral.id,
                    id_persona=expediente_laboral.id_persona,
                    fecha_ingreso=expediente_laboral.registrado_en,
                    detalle=lista_expediente

                )

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
        return expediente

    @classmethod
    async def buscar_por_id(cls, id: str) -> DetalleExpedienteSchema:

        detalle_expediente: ExpedienteLaboralSchema = None
        tipo_documento: TipoDocumentoSchema = None
        relacion_ies: RelacionIESSchema = None
        escalafon_nombramiento: TipoEscalafonNombramientoSchema = None
        categoria_contrato: CategoriaContratoProfesorSchema = None
        tiempo_dedicacion: TiempoDedicacionProfesorSchema = None
        tipo_funcionario: TipoFuncionarioSchema = None
        tipo_docente: TipoDocenteLOESSchema = None
        categoria_docente: CategoriaDocenteLOSEPSchema = None
        nivel: NivelEducativoSchema = None
        area: AreaInstitucionSchema = None
        sub_area: AreaInstitucionSchema = None
        tipo_contrato: TipoContratoSchema = None
        tipo_nombramiento: TipoNombramientoSchema = None
        

        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            detalle: DetalleExpedienteLaboral = None
            results = await async_db_session.execute(select(DetalleExpedienteLaboral).where(
                DetalleExpedienteLaboral.id == id
            ))

            detalle = results.scalar_one()
            if detalle:
                jerarquico = 'NO'
                concurso = 'NO'
                if Opciones.SI == detalle.puesto_jerarquico:
                    jerarquico = 'SI'
                if Opciones.SI == detalle.ingreso_concurso:
                    concurso = 'SI'
                result = await async_db_session.execute(select(TipoDocumento).where(TipoDocumento.id == detalle.id_tipo_documento))
                t_doc = result.scalar_one()
                tipo_documento = TipoDocumentoSchema(**t_doc.__dict__)
                result = await async_db_session.execute(select(RelacionIES).where(RelacionIES.id == detalle.id_relacion_ies))
                r_ies = result.scalar_one()
                relacion_ies = RelacionIESSchema(**r_ies.__dict__)
                if detalle.id_tipo_escalafon:
                    result = await async_db_session.execute(select(TipoEscalafonNombramiento).where(
                        TipoEscalafonNombramiento.id == detalle.id_tipo_escalafon))
                    t_es = result.scalar_one()
                    escalafon_nombramiento = TipoEscalafonNombramientoSchema(
                        **t_es.__dict__)
                if detalle.id_categoria_contrato:
                    result = await async_db_session.execute(select(CategoriaContratoProfesor).where(
                        CategoriaContratoProfesor.id == detalle.id_categoria_contrato))
                    t_ccp = result.scalar_one()
                    categoria_contrato = CategoriaContratoProfesorSchema(
                        **t_ccp.__dict__)
                if detalle.id_tiempo_dedicacion:
                    result = await async_db_session.execute(select(TiempoDedicacionProfesor).where(
                        TiempoDedicacionProfesor.id == detalle.id_tiempo_dedicacion))
                    t_d = result.scalar_one()
                    tiempo_dedicacion = TiempoDedicacionProfesorSchema(
                        **t_d.__dict__)
                if detalle.id_tipo_funcionario:
                    result = await async_db_session.execute(select(TipoFuncionario).where(
                        TipoFuncionario.id == detalle.id_tipo_funcionario))
                    t_f = result.scalar_one()
                    tipo_funcionario = TipoFuncionarioSchema(**t_f.__dict__)
                if detalle.id_tipo_docente:
                    result = await async_db_session.execute(select(TipoDocenteLOES).where(
                        TipoDocenteLOES.id == detalle.id_tipo_docente))
                    t_d = result.scalar_one()
                    tipo_docente = TipoDocenteLOESSchema(**t_d.__dict__)
                if detalle.id_categoria_docente:
                    result = await async_db_session.execute(select(CategoriaDocenteLOSEP).where(
                        CategoriaDocenteLOSEP.id == detalle.id_categoria_docente))
                    c_d = result.scalar_one()
                    categoria_docente = CategoriaDocenteLOSEPSchema(
                        **c_d.__dict__)
                result = await async_db_session.execute(select(AreaInstitucion).where(
                    AreaInstitucion.id == detalle.id_area))
                a_ins = result.scalar_one()
                area = AreaInstitucionSchema(**a_ins.__dict__)
                if detalle.id_sub_area:
                    result = await async_db_session.execute(select(AreaInstitucion).where(
                        AreaInstitucion.id == detalle.id_sub_area))
                    sa_ins = result.scalar_one()
                    sub_area = AreaInstitucionSchema(**sa_ins.__dict__)
                if detalle.id_nivel:
                    result = await async_db_session.execute(select(NivelEducativo).where(
                        NivelEducativo.id == detalle.id_nivel
                    ))
                    niv = result.scalar_one()
                    nivel = NivelEducativoSchema(**niv.__dict__)
                if detalle.id_tipo_contrato:
                    result = await async_db_session.execute(select(TipoContrato).where(TipoContrato.id == detalle.id_tipo_contrato))
                    t_contrato = result.scalar_one()
                    tipo_contrato = TipoContratoSchema(**t_contrato.__dict__)
                if detalle.id_tipo_nombramiento:
                    result = await async_db_session.execute(select(TipoNombramiento).where(TipoNombramiento.id == detalle.id_tipo_nombramiento))
                    t_nomb = result.scalar_one()
                    tipo_nombramiento = TipoNombramientoSchema(**t_nomb.__dict__)

                detalle_expediente = DetalleExpedienteSchema(
                    id=detalle.id,
                    id_expediente=detalle.id_expediente,
                    tipo_personal=TipoPersonal[detalle.tipo_personal.value],
                    tipo_documento=tipo_documento,
                    tipo_nombramiento = tipo_nombramiento,
                    tipo_contrato = tipo_contrato,
                    motivo_accion=detalle.motivo_accion,
                    descripcion = detalle.descripcion,
                    numero_documento=detalle.numero_documento,
                    contrato_relacionado=detalle.contrato_relacionado,
                    ingreso_concurso=concurso,
                    relacion_ies=relacion_ies,
                    escalafon_nombramiento=escalafon_nombramiento,
                    categoria_contrato=categoria_contrato,
                    tiempo_dedicacion=tiempo_dedicacion,
                    remuneracion_mensual=detalle.remuneracion_mensual,
                    remunerracion_hora=detalle.remuneracion_hora,
                    fecha_inicio=detalle.fecha_inicio,
                    fecha_fin=detalle.fecha_fin,
                    tipo_funcionario=tipo_funcionario,
                    cargo=detalle.cargo,
                    tipo_docente=tipo_docente,
                    categoria_docente=categoria_docente,
                    puesto_jerarquico=jerarquico,
                    horas_laborables_semanales=detalle.horas_laborables_semanales,
                    area=area,
                    sub_area=sub_area,
                    nivel=nivel



                )
                await async_db_session.close()

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return detalle_expediente

    @classmethod
    async def buscar_por_id_con_session(cls, id: str, async_db_session: AsyncDatabaseSession) -> DetalleExpedienteSchema:

        detalle_expediente: ExpedienteLaboralSchema = None
        tipo_documento: TipoDocumentoSchema = None
        relacion_ies: RelacionIESSchema = None
        escalafon_nombramiento: TipoEscalafonNombramientoSchema = None
        categoria_contrato: CategoriaContratoProfesorSchema = None
        tiempo_dedicacion: TiempoDedicacionProfesorSchema = None
        tipo_funcionario: TipoFuncionarioSchema = None
        tipo_docente: TipoDocenteLOESSchema = None
        categoria_docente: CategoriaDocenteLOSEPSchema = None
        nivel: NivelEducativoSchema = None
        area: AreaInstitucionSchema = None
        sub_area: AreaInstitucionSchema = None
        tipo_contrato: TipoContratoSchema = None
        tipo_nombramiento: TipoNombramientoSchema = None

        try:
            detalle: DetalleExpedienteLaboral = None
            results = await async_db_session.execute(select(DetalleExpedienteLaboral).where(
                DetalleExpedienteLaboral.id == id
            ))

            detalle = results.scalar_one()
            if detalle:
                jerarquico = 'NO'
                concurso = 'NO'
                if Opciones.SI == detalle.puesto_jerarquico:
                    jerarquico = 'SI'
                if Opciones.SI == detalle.ingreso_concurso:
                    concurso = 'SI'
                result = await async_db_session.execute(select(TipoDocumento).where(TipoDocumento.id == detalle.id_tipo_documento))
                t_doc = result.scalar_one()
                tipo_documento = TipoDocumentoSchema(**t_doc.__dict__)
                result = await async_db_session.execute(select(RelacionIES).where(RelacionIES.id == detalle.id_relacion_ies))
                r_ies = result.scalar_one()
                relacion_ies = RelacionIESSchema(**r_ies.__dict__)
                if detalle.id_tipo_escalafon:
                    result = await async_db_session.execute(select(TipoEscalafonNombramiento).where(
                        TipoEscalafonNombramiento.id == detalle.id_tipo_escalafon))
                    t_es = result.scalar_one()
                    escalafon_nombramiento = TipoEscalafonNombramientoSchema(
                        **t_es.__dict__)
                if detalle.id_categoria_contrato:
                    result = await async_db_session.execute(select(CategoriaContratoProfesor).where(
                        CategoriaContratoProfesor.id == detalle.id_categoria_contrato))
                    t_ccp = result.scalar_one()
                    categoria_contrato = CategoriaContratoProfesorSchema(
                        **t_ccp.__dict__)
                if detalle.id_tiempo_dedicacion:
                    result = await async_db_session.execute(select(TiempoDedicacionProfesor).where(
                        TiempoDedicacionProfesor.id == detalle.id_tiempo_dedicacion))
                    t_d = result.scalar_one()
                    tiempo_dedicacion = TiempoDedicacionProfesorSchema(
                        **t_d.__dict__)
                if detalle.id_tipo_funcionario:
                    result = await async_db_session.execute(select(TipoFuncionario).where(
                        TipoFuncionario.id == detalle.id_tipo_funcionario))
                    t_f = result.scalar_one()
                    tipo_funcionario = TipoFuncionarioSchema(**t_f.__dict__)
                if detalle.id_tipo_docente:
                    result = await async_db_session.execute(select(TipoDocenteLOES).where(
                        TipoDocenteLOES.id == detalle.id_tipo_docente))
                    t_d = result.scalar_one()
                    tipo_docente = TipoDocenteLOESSchema(**t_d.__dict__)
                if detalle.id_categoria_docente:
                    result = await async_db_session.execute(select(CategoriaDocenteLOSEP).where(
                        CategoriaDocenteLOSEP.id == detalle.id_categoria_docente))
                    c_d = result.scalar_one()
                    categoria_docente = CategoriaDocenteLOSEPSchema(
                        **c_d.__dict__)
                result = await async_db_session.execute(select(AreaInstitucion).where(
                    AreaInstitucion.id == detalle.id_area))
                a_ins = result.scalar_one()
                area = AreaInstitucionSchema(**a_ins.__dict__)
                if detalle.id_sub_area:
                    result = await async_db_session.execute(select(AreaInstitucion).where(
                        AreaInstitucion.id == detalle.id_sub_area))
                    sa_ins = result.scalar_one()
                    sub_area = AreaInstitucionSchema(**sa_ins.__dict__)
                if detalle.id_nivel:
                    result = await async_db_session.execute(select(NivelEducativo).where(
                        NivelEducativo.id == detalle.id_nivel
                    ))
                    niv = result.scalar_one()
                    nivel = NivelEducativoSchema(**niv.__dict__)
                if detalle.id_tipo_contrato:
                    result = await async_db_session.execute(select(TipoContrato).where(TipoContrato.id == detalle.id_tipo_contrato))
                    t_contrato = result.scalar_one()
                    tipo_contrato = TipoContratoSchema(**t_contrato.__dict__)
                if detalle.id_tipo_nombramiento:
                    result = await async_db_session.execute(select(TipoNombramiento).where(TipoNombramiento.id == detalle.id_tipo_nombramiento))
                    t_nomb = result.scalar_one()
                    tipo_nombramiento = TipoNombramientoSchema(**t_nomb.__dict__)

                detalle_expediente = DetalleExpedienteSchema(
                    id=detalle.id,
                    id_expediente=detalle.id_expediente,
                    tipo_personal=TipoPersonal[detalle.tipo_personal.value],
                    tipo_documento=tipo_documento,
                    tipo_nombramiento = tipo_nombramiento,
                    tipo_contrato = tipo_contrato,
                    motivo_accion=detalle.motivo_accion,
                    descripcion = detalle.descripcion,
                    numero_documento=detalle.numero_documento,
                    contrato_relacionado=detalle.contrato_relacionado,
                    ingreso_concurso=concurso,
                    relacion_ies=relacion_ies,
                    escalafon_nombramiento=escalafon_nombramiento,
                    categoria_contrato=categoria_contrato,
                    tiempo_dedicacion=tiempo_dedicacion,
                    remuneracion_mensual=detalle.remuneracion_mensual,
                    remunerracion_hora=detalle.remuneracion_hora,
                    fecha_inicio=detalle.fecha_inicio,
                    fecha_fin=detalle.fecha_fin,
                    tipo_funcionario=tipo_funcionario,
                    cargo=detalle.cargo,
                    tipo_docente=tipo_docente,
                    categoria_docente=categoria_docente,
                    puesto_jerarquico=jerarquico,
                    horas_laborables_semanales=detalle.horas_laborables_semanales,
                    area=area,
                    sub_area=sub_area,
                    nivel=nivel



                )

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return detalle_expediente

    @classmethod
    async def agregar_registro(cls, id_persona: str,
                               detalle_expediente: Union[DetalleExpedienteProfesorPostSchema, DetalleExpedienteFuncionarioPostSchema]) -> bool:
        registrado: bool = False
        try:

            expediente = await ExpedienteLaboral.filtarPor(id_persona=id_persona)

            if expediente:

                concurso = 'NO'

                if Opciones.SI == detalle_expediente.ingreso_concurso:
                    concurso = 'SI'
                if isinstance(detalle_expediente, DetalleExpedienteFuncionarioPostSchema):
                    jerarquico = 'NO'
                    if Opciones.SI == detalle_expediente.puesto_jerarquico:
                        jerarquico = 'SI'
                    registrado = await DetalleExpedienteLaboral.crear(
                        id_expediente=expediente[0][0].id,
                        tipo_personal=TP.FUNCIONARIO,
                        id_tipo_documento=detalle_expediente.tipo_documento,
                        id_tipo_contrato = detalle_expediente.tipo_contrato if detalle_expediente.tipo_contrato else None,
                        id_tipo_nombramiento = detalle_expediente.tipo_nombramiento if detalle_expediente.tipo_nombramiento else None,
                        motivo_accion=detalle_expediente.motivo_accion,
                        descripcion = detalle_expediente.descripcion,
                        numero_documento=detalle_expediente.numero_documento,
                        ingreso_concurso=concurso,
                        id_relacion_ies=detalle_expediente.relacion_ies,
                        fecha_inicio=detalle_expediente.fecha_inicio,
                        fecha_fin=detalle_expediente.fecha_fin,
                        id_area=detalle_expediente.area,
                        remuneracion_mensual=detalle_expediente.remuneracion_mensual,
                        id_sub_area=detalle_expediente.sub_area,
                        id_tipo_funcionario=detalle_expediente.tipo_funcionario,
                        cargo=detalle_expediente.cargo,
                        id_tipo_docente=detalle_expediente.tipo_docente,
                        id_categoria_docente=detalle_expediente.categoria_docente,
                        puesto_jerarquico=jerarquico,
                        horas_laborables_semanales=detalle_expediente.horas_laborables_semanales
                    )

                elif isinstance(detalle_expediente, DetalleExpedienteProfesorPostSchema):
                    rem_hora = 0
                    if detalle_expediente.remuneracion_hora is not None:
                        rem_hora = detalle_expediente.remuneracion_hora
                    registrado = await DetalleExpedienteLaboral.crear(
                        id_expediente=expediente[0][0].id,
                        id_tipo_documento=detalle_expediente.tipo_documento,
                        id_tipo_contrato = detalle_expediente.tipo_contrato if detalle_expediente.tipo_contrato else None,
                        id_tipo_nombramiento = detalle_expediente.tipo_nombramiento if detalle_expediente.tipo_nombramiento else None,
                        tipo_personal=TP.PROFESOR,
                        motivo_accion=detalle_expediente.motivo_accion,
                        descripcion = detalle_expediente.descripcion,
                        numero_documento=detalle_expediente.numero_documento,
                        ingreso_concurso=concurso,
                        id_relacion_ies=detalle_expediente.relacion_ies,
                        fecha_inicio=detalle_expediente.fecha_inicio,

                        fecha_fin=detalle_expediente.fecha_fin,
                        id_area=detalle_expediente.area,
                        remuneracion_mensual=detalle_expediente.remuneracion_mensual,
                        id_sub_area=detalle_expediente.sub_area,
                        contrato_relacionado=detalle_expediente.contrato_relacionado,
                        id_tipo_escalafon=detalle_expediente.escalafon_nombramiento,
                        id_categoria_contrato=detalle_expediente.categoria_contrato,
                        id_tiempo_dedicacion=detalle_expediente.tiempo_dedicacion,
                        remuneracion_hora=rem_hora,
                        id_nivel=detalle_expediente.nivel)

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return registrado

    @classmethod
    async def actualizar_registro(cls,
                                  detalle_expediente=Union[DetalleExpedienteProfesorPutSchema, DetalleExpedienteFuncionarioPutSchema]):
        actualizado: bool = false
        try:
            result = await DetalleExpedienteLaboral.obtener(id=detalle_expediente.id)

            if result:
                jerarquico = 'NO'
                concurso = 'NO'
               
                if Opciones.SI == detalle_expediente.ingreso_concurso:
                    concurso = 'SI'

                if isinstance(detalle_expediente, DetalleExpedienteFuncionarioPutSchema):
                    if Opciones.SI == detalle_expediente.puesto_jerarquico:
                        jerarquico = 'SI'

                    actualizado = await DetalleExpedienteLaboral.actualizar(
                        id=detalle_expediente.id,
                        tipo_personal=TP.FUNCIONARIO,
                        id_tipo_documento=detalle_expediente.tipo_documento,
                        id_tipo_contrato = detalle_expediente.tipo_contrato if detalle_expediente.tipo_contrato else None,
                        id_tipo_nombramiento = detalle_expediente.tipo_nombramiento if detalle_expediente.tipo_nombramiento else None,
                        motivo_accion=detalle_expediente.motivo_accion,
                        descripcion = detalle_expediente.descripcion,
                        numero_documento=detalle_expediente.numero_documento,
                        ingreso_concurso=concurso,
                        id_relacion_ies=detalle_expediente.relacion_ies,
                        fecha_inicio=detalle_expediente.fecha_inicio,
                        fecha_fin=detalle_expediente.fecha_fin,
                        id_area=detalle_expediente.area,
                        remuneracion_mensual=detalle_expediente.remuneracion_mensual,
                        id_sub_area=detalle_expediente.sub_area,
                        id_tipo_funcionario=detalle_expediente.tipo_funcionario,
                        cargo=detalle_expediente.cargo,
                        id_tipo_docente=detalle_expediente.tipo_docente,
                        id_categoria_docente=detalle_expediente.categoria_docente,
                        puesto_jerarquico=jerarquico,
                        horas_laborables_semanales=detalle_expediente.horas_laborables_semanales,
                        contrato_relacionado='',
                        id_tipo_escalafon=None,
                        id_categoria_contrato=None,
                        id_tiempo_dedicacion=None,
                        remuneracion_hora=0
                    )

                elif isinstance(detalle_expediente, DetalleExpedienteProfesorPutSchema):
                    rem_hora = 0
                    if detalle_expediente.remuneracion_hora is not None:
                        rem_hora = detalle_expediente.remuneracion_hora
                    actualizado = await DetalleExpedienteLaboral.actualizar(
                        id=detalle_expediente.id,
                        id_tipo_documento=detalle_expediente.tipo_documento,
                        id_tipo_contrato = detalle_expediente.tipo_contrato if detalle_expediente.tipo_contrato else None,
                        id_tipo_nombramiento = detalle_expediente.tipo_nombramiento if detalle_expediente.tipo_nombramiento else None,
                        tipo_personal=TP.PROFESOR,
                        motivo_accion=detalle_expediente.motivo_accion,
                        descripcion = detalle_expediente.descripcion,

                        numero_documento=detalle_expediente.numero_documento,
                        ingreso_concurso=detalle_expediente.ingreso_concurso,
                        id_relacion_ies=detalle_expediente.relacion_ies,
                        fecha_inicio=detalle_expediente.fecha_inicio,

                        fecha_fin=detalle_expediente.fecha_fin,
                        id_area=detalle_expediente.area,
                        remuneracion_mensual=detalle_expediente.remuneracion_mensual,
                        id_sub_area=detalle_expediente.sub_area,
                        contrato_relacionado=detalle_expediente.contrato_relacionado,
                        id_tipo_escalafon=detalle_expediente.escalafon_nombramiento,
                        id_categoria_contrato=detalle_expediente.categoria_contrato,
                        id_tiempo_dedicacion=detalle_expediente.tiempo_dedicacion,
                        remuneracion_hora=rem_hora,
                        id_nivel=detalle_expediente.nivel,

                        id_tipo_funcionario=None,
                        cargo='',
                        id_tipo_docente=None,
                        id_categoria_docente=None,
                        puesto_jerarquico=None,
                        horas_laborables_semanales=0)

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return actualizado

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await DetalleExpedienteLaboral.eliminar(id=id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
