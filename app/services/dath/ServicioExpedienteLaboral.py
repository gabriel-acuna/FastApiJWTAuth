import re
from typing import List, Union

from sqlalchemy.sql.elements import False_
from app.models.dath.modelos import ExpedienteLaboral, DetalleExpedianteLaboral
from app.models.core.modelos_principales import TipoDocumento, RelacionIES, TipoEscalafonNombramiento, TiempoDedicacionProfesor
from app.models.core.modelos_principales import CategoriaContratoProfesor, TipoFuncionario, TipoDocenteLOES
from app.models.core.modelos_principales import CategoriaDocenteLOSEP, NivelEducativo, AreaInstitucion
from app.schemas.dath.DetalleExpedienteSchema import *
from app.schemas.dath.ExpedianteLaboralSachema import ExpedienteLaboralSchema
from app.database.conf import async_db_session
import logging

class ServicioExpedienteLaboral():

    @classmethod
    async def listar(cls, id_persona:str) -> ExpedienteLaboralSchema:
        expediente:ExpedienteLaboralSchema = None
        lista_expediente: List[DetalleExpedienteSchema] = []
        try:
            expediente_laboral = await ExpedienteLaboral.filtarPor(id_persona=id_persona)
            if expediente_laboral:
                filas = DetalleExpedianteLaboral.filtarPor(id_expediente = expediente_laboral[0][0].id)
                for fila in filas:
                    pass
                expediente = ExpedienteLaboral(
                    id = expediente[0][0].id,
                    id_persona = expediente[0][0].id_persona,
                    fecha_ingreso = expediente[0][0].registrado_en,
                    detalle = lista_expediente

                )

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return expediente
    
    @classmethod
    async def buscar_por_id(cls, id_persona:str) -> DetalleExpedienteSchema:
        detalle_expediente:ExpedienteLaboralSchema = None
        try:
            pass
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return detalle_expediente
    

    @classmethod
    async def agregar_registro(cls, id_persona:str,
        detalle_expediente: Union[DetalleExpedienteDocentePost, DetalleExpedianteFuncionarioPost]) -> bool:
        registrado: bool = False
        try:
            expediente = await ExpedienteLaboral.filtarPor(id_persona=id_persona)
            if expediente:
                async_db_session.init()
                detalle = DetalleExpedianteLaboral()
                detalle.id_expediente= expediente[0][0].id
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
                if detalle_expediente.remuneracion_hora  is not None:
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
        detalle_expediente = Union(DetalleExpedienteDocentePut, DetalleExpedianteFuncionarioPut)):
        try:
            result = await DetalleExpedianteLaboral.obtener(id= detalle_expediente.id)
            if result:
                detalle = result[0]
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
                if detalle_expediente.remuneracion_hora  is not None:
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
            

    

