import logging
from app.services.dath.ServicioDireccionDomicilio import ServicioDireccionDomicilio
from app.models.core.modelos_principales import Nacionalidad
from app.services.core.ServicioDiscapacidad import ServicioDiscapacidad
from app.schemas.core.PaisSchema import PaisSchema
from app.services.core.ServicioEtnia import ServicioEtnia
from app.services.core.ServicioPais import ServicioPais
from typing import List
from sqlalchemy.sql.elements import or_
from sqlalchemy.sql.expression import delete, select
from app.schemas.dath.InformacionPersonalSchema import *
from app.models.dath.modelos import ExpedienteLaboral, InformacionPersonal, DireccionDomicilio
from app.services.core.ServicioNacionalidad import ServicioNacionalidad
from app.database.conf import async_db_session
from app.services.core.ServicioEstadoCivil import ServicioEstadoCivil
from app.schemas.dath.DireccionSchema import *


class ServicioInformacionPersonal():

    @classmethod
    async def listar(cls) -> List[InformacionPersonalSchema]:
        personal_ies: List[InformacionPersonalSchema] = []
        try:
            filas = await InformacionPersonal.listar()
            for fila in filas:
                nacionalidad: NacionalidadSchema = None
                persona = fila[0]
                etnia = await ServicioEtnia.buscar_por_id(persona.id_etnia)
                discapacidad = await ServicioDiscapacidad.buscar_por_id(persona.id_discapacidad)
                pais = await ServicioPais.buscar_por_id(persona.id_pais_origen)
                estado_civil = await ServicioEstadoCivil.buscar_por_id(persona.id_estado_civil)
                if persona.id_nacionalidad is not None:
                    nac = ServicioNacionalidad.buscar_por_id(
                        persona.id_nacionalidad)
                    nacionalidad = NacionalidadSchema(**nac[0].__dict__)
                direccion = await ServicioDireccionDomicilio.buscar_por_id_persona(persona.identificacion)
                await async_db_session.init()
                results = await async_db_session.execute(
                    select(ExpedienteLaboral).filter_by(
                            id_persona=persona.identificacion
                    )
                )
                expediente = results.scalar_one()
                await async_db_session.close()
                personal_ies.append(
                    InformacionPersonalSchema(
                        tipo_identificacion=TipoIdentificacion[persona.tipo_identificacion.value],
                        identificacion=persona.identificacion,
                        primer_nombre=persona.primer_nombre,
                        segundo_nombre=persona.segundo_nombre,
                        primer_apellido=persona.primer_apellido,
                        segundo_apellido=persona.segundo_apellido,
                        sexo=Sexo[persona.sexo.value],
                        fecha_nacimiento=persona.fecha_nacimiento,
                        edad=persona.calcular_edad(),
                        pais_origen=PaisSchema(**pais[0].__dict__),
                        estado_civil=EstadoCivilSchema(
                            **estado_civil[0].__dict__),
                        discapacidad=DiscapacidadSchema(
                            **discapacidad[0].__dict__),
                        carnet_conadis=persona.carnet_conadis,
                        porcentaje_discapacidad=persona.porcentaje_discapacidad,
                        etnia=EtniaSchema(**etnia[0].__dict__),
                        nacionalidad=nacionalidad,
                        correo_institucional=persona.correo_institucional,
                        correo_personal=persona.correo_institucional,
                        telefono_domicilio=persona.telefono_domicilio,
                        telefono_movil=persona.telefono_movil,
                        direccion_domicilio=direccion,
                        tipo_sangre=persona.tipo_sangre,
                        licencia_conduccion=persona.lincencia_conduccion,
                        fecha_ingreso = expediente.registrado_en


                    )
                )

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return personal_ies

    @classmethod
    async def buscar_por_id(cls, id: str) -> InformacionPersonalSchema:
        informacion_personal: InformacionPersonalSchema = None
        try:
            respuesta = await InformacionPersonal.filtarPor(identificacion=id)
            persona: InformacionPersonal = None
            nacionalidad: NacionalidadSchema = None
            direccion: DireccionSchema = None
            if respuesta:

                persona = respuesta[0][0]
                etnia = await ServicioEtnia.buscar_por_id(persona.id_etnia)
                discapacidad = await ServicioDiscapacidad.buscar_por_id(persona.id_discapacidad)
                pais = await ServicioPais.buscar_por_id(persona.id_pais_origen)
                estado_civil = await ServicioEstadoCivil.buscar_por_id(persona.id_estado_civil)
                if persona.id_nacionalidad is not None:
                    nac = ServicioNacionalidad.buscar_por_id(
                        persona.id_nacionalidad)
                    nacionalidad = NacionalidadSchema(**nac[0].__dict__)
                direccion = await ServicioDireccionDomicilio.buscar_por_id_persona(persona.identificacion)
                await async_db_session.init()
                results = await async_db_session.execute(
                    select(ExpedienteLaboral).filter_by(
                        id_persona=id
                    )
                )
            
                expediente = results.scalar_one()
                await async_db_session.close()
                informacion_personal = InformacionPersonalSchema(
                    tipo_identificacion=TipoIdentificacion[persona.tipo_identificacion.value],
                    identificacion=persona.identificacion,
                    primer_nombre=persona.primer_nombre,
                    segundo_nombre=persona.segundo_nombre,
                    primer_apellido=persona.primer_apellido,
                    segundo_apellido=persona.segundo_apellido,
                    sexo=Sexo[persona.sexo.value],
                    fecha_nacimiento=persona.fecha_nacimiento,
                    edad=persona.calcular_edad(),
                    pais_origen=PaisSchema(**pais[0].__dict__),
                    estado_civil=EstadoCivilSchema(**estado_civil[0].__dict__),
                    discapacidad=DiscapacidadSchema(
                        **discapacidad[0].__dict__),
                    carnet_conadis=persona.carnet_conadis,
                    porcentaje_discapacidad=persona.porcentaje_discapacidad,
                    etnia=EtniaSchema(**etnia[0].__dict__),
                    nacionalidad=nacionalidad,
                    correo_institucional=persona.correo_institucional,
                    correo_personal=persona.correo_institucional,
                    telefono_domicilio=persona.telefono_domicilio,
                    telefono_movil=persona.telefono_movil,
                    direccion_domicilio=direccion,
                    tipo_sangre=persona.tipo_sangre,
                    licencia_conduccion=persona.lincencia_conduccion,
                    fecha_ingreso = expediente.registrado_en


                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return informacion_personal

    @classmethod
    async def agregar_registro(cls, persona: InformacionPersonalPostSchema) -> bool:
        regsitrado = False
        try:
            await async_db_session.init()

            informacion_personal = InformacionPersonal()
            informacion_personal.tipo_identificacion = persona.tipo_identificacion
            informacion_personal.identificacion = persona.identificacion
            informacion_personal.primer_nombre = persona.primer_nombre
            informacion_personal.segundo_nombre = persona.segundo_nombre
            informacion_personal.primer_apellido = persona.primer_apellido
            informacion_personal.segundo_apellido = persona.segundo_apellido
            informacion_personal.sexo = persona.sexo
            informacion_personal.fecha_nacimiento = persona.fecha_nacimiento
            informacion_personal.id_pais_origen = persona.pais_origen
            informacion_personal.id_estado_civil = persona.estado_civil
            informacion_personal.id_etnia = persona.etnia
            if persona.nacionalidad:
                informacion_personal.id_nacionalidad = persona.nacionalidad
            informacion_personal.id_discapacidad = persona.discapacidad
            if persona.carnet_conadis:
                informacion_personal.carnet_conadis = persona.carnet_conadis
            informacion_personal.porcentaje_discapacidad = persona.porcentaje_discapacidad
            informacion_personal.correo_institucional = persona.correo_institucional
            informacion_personal.correo_personal = persona.correo_personal
            if persona.telefono_domicilio:
                informacion_personal.telefono_domicilio = persona.telefono_domicilio
            informacion_personal.telefono_movil = persona.telefono_movil
            informacion_personal.tipo_sangre = persona.tipo_sangre
            if persona.licencia_conduccion:
                informacion_personal.lincencia_conduccion = persona.licencia_conduccion
            informacion_personal.direccion_domicilio = DireccionDomicilio(
                id_canton=persona.direccion_domicilio.id_canton,
                id_provincia=persona.direccion_domicilio.id_provincia,
                parroquia=persona.direccion_domicilio.parroquia,
                calle1=persona.direccion_domicilio.calle1,
                calle2=persona.direccion_domicilio.calle2,
                referencia=persona.direccion_domicilio.referencia)
            async_db_session.add(informacion_personal)
            await async_db_session.commit()
            async_db_session.add(
                ExpedienteLaboral(
                    id_persona=informacion_personal.identificacion,
                    registrado_en=persona.fecha_ingreso)

            )
            await async_db_session.commit()
            regsitrado = True
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
        return regsitrado

    @classmethod
    async def actualizar_registro(cls, persona: InformacionPersonalPutSchema, id: str):
        resp = False
        try:
            await async_db_session.init()

            results = await async_db_session.execute(
                select(InformacionPersonal).filter_by(identificacion=id))

            informacion_personal = results.scalar_one()

            results1 = await async_db_session.execute(
                select(DireccionDomicilio).filter_by(id_persona=id))
            direccion = results1.scalar_one()
            direccion.id_provincia = persona.direccion_domicilio.id_provincia
            direccion.id_canton = persona.direccion_domicilio.id_canton
            direccion.calle1 = persona.direccion_domicilio.calle1
            direccion.calle2 = persona.direccion_domicilio.calle2
            direccion.referencia = persona.direccion_domicilio.referencia

            results2 = await async_db_session.execute(
                select(ExpedienteLaboral).filter_by(
                    id_persona=id
                )
            )
            expediente = results2.scalar_one()
            persona.tipo_identificacion = persona.tipo_identificacion
            informacion_personal.primer_nombre = persona.primer_nombre
            informacion_personal.segundo_nombre = persona.segundo_nombre
            informacion_personal.primer_apellido = persona.primer_apellido
            informacion_personal.segundo_apellido = persona.segundo_apellido
            informacion_personal.sexo = persona.sexo
            informacion_personal.fecha_nacimiento = persona.fecha_nacimiento
            informacion_personal.id_pais_origen = persona.pais_origen
            informacion_personal.id_estado_civil = persona.estado_civil
            informacion_personal.id_etnia = persona.etnia
            if persona.nacionalidad:
                informacion_personal.id_nacionalidad = persona.nacionalidad
            else:
                informacion_personal.id_nacionalidad = None
            informacion_personal.id_discapacidad = persona.discapacidad
            if persona.carnet_conadis:
                informacion_personal.carnet_conadis = persona.carnet_conadis
            informacion_personal.porcentaje_discapacidad = persona.porcentaje_discapacidad
            informacion_personal.correo_institucional = persona.correo_institucional
            informacion_personal.correo_personal = persona.correo_personal
            if persona.telefono_domicilio is None:
                persona.telefono_domicilio = '0000000000'
            informacion_personal.telefono_domicilio = persona.telefono_domicilio
            informacion_personal.tipo_sangre = persona.tipo_sangre
            if persona.licencia_conduccion:
                informacion_personal.lincencia_conduccion = persona.licencia_conduccion
            informacion_personal.direccion_domicilio = direccion
            expediente.registrado_en = persona.fecha_ingreso

            await async_db_session.commit()
            resp = True

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
        return resp

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        elminado = False
        try:
            await async_db_session.init()
            query = delete(DireccionDomicilio).where(
                DireccionDomicilio.id_persona == id)
            await async_db_session.execute(query)
            query1 = delete(ExpedienteLaboral).where(
                ExpedienteLaboral.id_persona == id)
            await async_db_session.execute(query1)
          
            query2 = delete(InformacionPersonal).where(
                InformacionPersonal.identificacion == id)
            await async_db_session.execute(query2)

            await async_db_session.commit()
            elminado = True
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()

        return elminado

    @classmethod
    async def existe(cls, **kwargs) -> bool:
        try:
            await async_db_session.init()
            query = select(InformacionPersonal).filter(or_(
                InformacionPersonal.identificacion == kwargs['id'],
                InformacionPersonal.correo_institucional == kwargs['correo_institucional']))
            results = await async_db_session.execute(query)
            persona = results.all()
            if persona:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
