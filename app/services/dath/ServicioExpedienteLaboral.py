from typing import List, Union
from app.models.dath.modelos import ExpedienteLaboral, DetalleExpedianteLaboral
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
            expediente_laboral = await ExpedienteLaboral.filtarPor(id_persona=id_persona)
            if expediente_laboral:
                filas = await DetalleExpedianteLaboral.filtarPor(
                    id_expediente=expediente_laboral[0][0].id)
                for fila in filas:
                    detalle = await ServicioExpedienteLaboral.buscar_por_id(fila[0].id)
                    if detalle:
                        lista_expediente.add(detalle)
                expediente = ExpedienteLaboralSchema(
                    id=expediente_laboral[0][0].id,
                    id_persona=expediente_laboral[0][0].id_persona,
                    fecha_ingreso=expediente_laboral[0][0].registrado_en,
                    detalle=lista_expediente

                )

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
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

        try:
            detalle = DetalleExpedianteLaboral.obtener(id=id)
            if detalle:
                t_doc = await TipoDocumento.obtener(id=detalle[0].id_tipo_documento)
                tipo_documento = TipoDocumentoSchema(**t_doc[0].__dict__)
                r_ies = await RelacionIES.obtener(id=detalle[0].id_relacion_ies)
                relacion_ies = RelacionIESSchema(**r_ies[0].__dict__)
                if detalle[0].id_tipo__escalafon:
                    t_es = await TipoEscalafonNombramiento.obtener(id=detalle[0].id_tipo_esclafon)
                    escalafon_nombramiento = TipoEscalafonNombramientoSchema(
                        **t_es[0].__dict__)
                if detalle[0].id_categoria_contrato:
                    t_ccp = await CategoriaContratoProfesor.obtener(id=detalle[0].id_categoria_contrato)
                    categoria_contrato = CategoriaContratoProfesorSchema(
                        **t_ccp.__dict__)
                if detalle[0].id_tiempo_dedicacion:
                    t_d = await TiempoDedicacionProfesor.obtener(id=detalle[0].id_tiempo_dedicacion)
                    tiempo_dedicacion = TiempoDedicacionProfesorSchema(
                        **t_d.__dict__)
                if detalle[0].id_tipo_funcionario:
                    t_f = await TipoFuncionario.obtener(id=detalle[0].id_tipo_funcionario)
                    tipo_funcionario = TipoFuncionarioSchema(**t_f[0].__dict__)
                if detalle[0].id_tipo_docente:
                    t_d = TipoDocenteLOES.obtener(
                        id=detalle[0].id_tipo_docente)
                    tipo_docente = TipoDocenteLOESSchema(**t_d[0].__dict__)
                if detalle[0].id_categoria_docente:
                    c_d = await CategoriaDocenteLOSEP.obtener(id=detalle[0].id_categoria_docente)
                    categoria_docente = CategoriaDocenteLOSEPSchema(
                        **c_d[0].__dict__)
                a_ins = await AreaInstitucion.obtener(id=detalle[0].id_area)
                area = AreaInstitucionSchema(**a_ins[0].__dict__)
                if detalle[0].id_sub_area:
                    sa_ins = await AreaInstitucion.obtener(id=detalle[0].id_sub_area)
                    sub_area = AreaInstitucionSchema(**sa_ins.__dict__)
                if detalle[0].id_nivel:
                    niv = await NivelEducativo.obtener(
                        id=detalle[0].id_nivel
                    )
                    nivel = NivelEducativoSchema(**niv[0].__dict__)

                detalle_expediente = DetalleExpedienteSchema(
                    id=detalle[0].id,
                    id_expediente=detalle[0].id_expediente,
                    tipo_personal=TipoPersonal[detalle[0].tipo_personal.value],
                    tipo_documento=tipo_documento,
                    motivo_accion=detalle[0].motivo_accion,
                    numero_documento=detalle[0].numero_documento,
                    contrato_relacionado=detalle[0].contrato_relacionado,
                    ingreso_concurso=detalle[0].ingreso_concurso,
                    relacion_ies=relacion_ies,
                    escalafon_nombramiento=escalafon_nombramiento,
                    categoria_contrato=categoria_contrato,
                    tiempo_dedicacion=tiempo_dedicacion,
                    remuneracion_mensual=detalle[0].remuneracion_mensual,
                    remunerracion_hora=detalle[0].remuneracion_hora,
                    fecha_inicio=detalle[0].fecha_inicio,
                    fecha_fin=detalle[0].fecha_fin,
                    tipo_funcionario=tipo_funcionario,
                    cargo=detalle[0].cargo,
                    tipo_docente=tipo_docente,
                    categoria_docente=categoria_docente,
                    puesto_jerarquico=detalle[0].puesto_jerarquico,
                    horas_laborables_semanales=detalle[0].horas_laborables_semanales,
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
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                detalle = DetalleExpedianteLaboral()
                detalle.id_expediente = expediente[0][0].id
                detalle.id_tipo_documento = detalle_expediente.tipo_documento
                if detalle_expediente.motivo_accion is not None:
                    detalle.motivo_accion = detalle_expediente.motivo_accion
                detalle.numero_documento = detalle_expediente.numero_documento
                if detalle_expediente.contrato_relacionado is not None:
                    detalle.contrato_relacionado = detalle.contrato_relacionado
                detalle.ingreso_concurso = detalle_expediente.ingreso_concurso
                detalle.id_relacion_ies = detalle_expediente.relacion_ies
                if detalle_expediente.escalafon_nombramiento is not None:
                    detalle.id_tipo_escalafon = detalle_expediente.escalafon_nombramiento

                if detalle_expediente.categoria_contrato is not None:
                    detalle.id_categoria_contrato = detalle_expediente.categoria_contrato
                if detalle_expediente.tiempo_dedicacion is not None:
                    detalle.id_tiempo_dedicacion = detalle_expediente.tiempo_dedicacion
                detalle.remuneracion_mensual = detalle_expediente.remuneracion_mensual
                if detalle_expediente.remuneracion_hora is not None:
                    detalle.remuneracion_hora = detalle_expediente.remuneracion_hora
                detalle.fecha_fin = detalle_expediente.fecha_inicio
                if detalle_expediente.fecha_fin is not None:
                    detalle.fecha_fin = detalle_expediente.fecha_fin
                if detalle_expediente.tipo_funcionario is not None:
                    detalle.id_tipo_funcionario = detalle_expediente.tipo_funcionario
                if detalle_expediente.cargo is not None:
                    detalle.cargo = detalle_expediente.cargo
                if detalle_expediente.tipo_docente is not None:
                    detalle.id_tipo_docente = detalle_expediente.tipo_docente
                if detalle_expediente.categoria_docente is not None:
                    detalle.id_categoria_docente = detalle_expediente.categoria_docente

                if detalle_expediente.puesto_jerarquico is not None:
                    detalle.puesto_jerarquico = detalle_expediente.puesto_jerarquico
                if detalle_expediente.horas_laborables_semanales is not None:
                    detalle.horas_laborables_semanales = detalle_expediente.horas_laborables_semanales
                if detalle_expediente.nivel is not None:
                    detalle.id_nivel = detalle_expediente.nivel
                detalle.id_area = detalle_expediente.area
                if detalle_expediente.sub_area is not None:
                    detalle.id_sub_area = detalle_expediente.sub_area

                await async_db_session.add(detalle)
                await async_db_session.commit()

                registrado = True
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            async_db_session.close()
        return registrado

    @classmethod
    async def actualizar_registro(
            detalle_expediente=Union[DetalleExpedienteProfesorPutSchema, DetalleExpedienteFuncionarioPutSchema]):
        try:
            result = await DetalleExpedianteLaboral.obtener(id=detalle_expediente.id)
            if result:
                detalle = result[0]
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                detalle.id_tipo_documento = detalle_expediente.tipo_documento
                if detalle_expediente.motivo_accion is not None:
                    detalle.motivo_accion = detalle_expediente.motivo_accion
                detalle.numero_documento = detalle_expediente.numero_documento
                if detalle_expediente.contrato_relacionado is not None:
                    detalle.contrato_relacionado = detalle.contrato_relacionado
                detalle.ingreso_concurso = detalle_expediente.ingreso_concurso
                detalle.id_relacion_ies = detalle_expediente.relacion_ies
                if detalle_expediente.escalafon_nombramiento is not None:
                    detalle.id_tipo_escalafon = detalle_expediente.escalafon_nombramiento

                if detalle_expediente.categoria_contrato is not None:
                    detalle.id_categoria_contrato = detalle_expediente.categoria_contrato
                if detalle_expediente.tiempo_dedicacion is not None:
                    detalle.id_tiempo_dedicacion = detalle_expediente.tiempo_dedicacion
                detalle.remuneracion_mensual = detalle_expediente.remuneracion_mensual
                if detalle_expediente.remuneracion_hora is not None:
                    detalle.remuneracion_hora = detalle_expediente.remuneracion_hora
                detalle.fecha_fin = detalle_expediente.fecha_inicio
                if detalle_expediente.fecha_fin is not None:
                    detalle.fecha_fin = detalle_expediente.fecha_fin
                if detalle_expediente.tipo_funcionario is not None:
                    detalle.id_tipo_funcionario = detalle_expediente.tipo_funcionario
                if detalle_expediente.cargo is not None:
                    detalle.cargo = detalle_expediente.cargo
                if detalle_expediente.tipo_docente is not None:
                    detalle.id_tipo_docente = detalle_expediente.tipo_docente
                if detalle_expediente.categoria_docente is not None:
                    detalle.id_categoria_docente = detalle_expediente.categoria_docente

                if detalle_expediente.puesto_jerarquico is not None:
                    detalle.puesto_jerarquico = detalle_expediente.puesto_jerarquico
                if detalle_expediente.horas_laborables_semanales is not None:
                    detalle.horas_laborables_semanales = detalle_expediente.horas_laborables_semanales
                if detalle_expediente.nivel is not None:
                    detalle.id_nivel = detalle_expediente.nivel
                detalle.id_area = detalle_expediente.area
                if detalle_expediente.sub_area is not None:
                    detalle.id_sub_area = detalle_expediente.sub_area

                await async_db_session.commit()

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()


    async def eliminar_registro(id:str) -> bool:
        try:
            return await ServicioExpedienteLaboral.eliminar_registro(id=id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

