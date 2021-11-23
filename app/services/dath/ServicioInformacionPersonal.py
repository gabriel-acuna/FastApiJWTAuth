import logging
from app.services.dath.ServicioContactoEmergencia import ServicioContactoEmergencia
from app.services.dath.ServicioDireccionDomicilio import ServicioDireccionDomicilio
from app.models.core.modelos_principales import Discapacidad, EstadoCivil, Etnia, Nacionalidad, Pais
from app.schemas.core.PaisSchema import PaisSchema
from typing import List
from sqlalchemy.sql.elements import or_
from sqlalchemy.sql.expression import delete, select
from app.schemas.dath.InformacionPersonalSchema import *
from app.schemas.dath.InformacionBancariaSchema import *
from app.models.dath.modelos import ContactoEmergencia, ExpedienteLaboral, InformacionBancaria, InformacionPersonal, DireccionDomicilio
from app.database.conf import AsyncDatabaseSession
from app.schemas.dath.DireccionSchema import *

 
class ServicioInformacionPersonal():

    @classmethod
    async def listar(cls) -> List[InformacionPersonalSchema]:
        personal_ies: List[InformacionPersonalSchema] = []
        try:
            filas = await InformacionPersonal.listar()
            for fila in filas:

                persona = fila[0]
                personal = await ServicioInformacionPersonal.buscar_por_id(id=persona.identificacion)
                personal_ies.append(personal)
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
            cuenta_bancaria: InformacionBancariaSchema
            persona: InformacionPersonal
            if respuesta:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                persona = respuesta[0][0]
                res = await async_db_session.execute(
                    select(Etnia).where(
                        Etnia.id == persona.id_etnia
                    ))
                etnia = res.scalar_one()
                res = await async_db_session.execute(
                    select(Discapacidad).where(
                        Discapacidad.id == persona.id_discapacidad
                    )
                )
                discapacidad = res.scalar_one()
                res = await async_db_session.execute(
                    select(Pais).where(
                        Pais.id == persona.id_pais_origen
                    )
                )
                pais = res.scalar_one()
                res = await async_db_session.execute(
                    select(EstadoCivil).where(
                        EstadoCivil.id == persona.id_estado_civil
                    )
                )
                estado_civil = res.scalar_one()
                res = await async_db_session.execute(
                    select(Nacionalidad).where(
                        Nacionalidad.id == persona.id_nacionalidad
                    )
                )
                nac = res.scalar_one()
                nacionalidad = NacionalidadSchema(**nac.__dict__)

                direccion = await ServicioDireccionDomicilio.buscar_por_id_persona(persona.identificacion)
                contacto_emergencia = await ServicioContactoEmergencia.buscar_por_id_persona(persona.identificacion)
                res = await async_db_session.execute(select(InformacionBancaria).filter_by(id_persona=persona.identificacion))
                info_ban = res.all()
                cuenta_bancaria = InformacionBancariaSchema(
                    id=info_ban[0][0].id,
                    institucion_financiera= info_ban[0][0].institucion_financiera,
                    tipo_cuenta = TipoCuenta[info_ban[0][0].tipo_cuenta.value],
                    numero_cuenta = info_ban[0][0].numero_cuenta )   if info_ban else None
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
                    pais_origen=PaisSchema(**pais.__dict__),
                    estado_civil=EstadoCivilSchema(**estado_civil.__dict__),
                    discapacidad=DiscapacidadSchema(
                        **discapacidad.__dict__),
                    carnet_conadis=persona.carnet_conadis,
                    porcentaje_discapacidad=persona.porcentaje_discapacidad,
                    etnia=EtniaSchema(**etnia.__dict__),
                    nacionalidad=nacionalidad,
                    correo_institucional=persona.correo_institucional,
                    correo_personal=persona.correo_personal,
                    telefono_domicilio=persona.telefono_domicilio,
                    telefono_movil=persona.telefono_movil,
                    direccion_domicilio=direccion,
                    contacto_emergencia=contacto_emergencia,
                    informacion_bancaria=cuenta_bancaria,
                    tipo_sangre=persona.tipo_sangre,
                    licencia_conduccion=persona.lincencia_conduccion,
                    tipo_licencia=TipoLicenciaConduccion[
                        persona.tipo_licencia_conduccion.value] if persona.tipo_licencia_conduccion is not None else None,
                    fecha_ingreso=expediente.registrado_en


                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return informacion_personal

    @classmethod
    async def buscar_por_correo_institucional(cls, correo_institucional: str) -> InformacionPersonalSchema:
        informacion_personal: InformacionPersonalSchema = None
        try:
            respuesta = await InformacionPersonal.filtarPor(correo_institucional=correo_institucional)
            persona: InformacionPersonal = None
            nacionalidad: NacionalidadSchema = None
            direccion: DireccionSchema = None
            persona: InformacionPersonal
            if respuesta:
                async_db_session = AsyncDatabaseSession()
                await async_db_session.init()
                persona = respuesta[0][0]
                res = await async_db_session.execute(
                    select(Etnia).where(
                        Etnia.id == persona.id_etnia
                    ))
                etnia = res.scalar_one()
                res = await async_db_session.execute(
                    select(Discapacidad).where(
                        Discapacidad.id == persona.id_discapacidad
                    )
                )
                discapacidad = res.scalar_one()
                res = await async_db_session.execute(
                    select(Pais).where(
                        Pais.id == persona.id_pais_origen
                    )
                )
                pais = res.scalar_one()
                res = await async_db_session.execute(
                    select(EstadoCivil).where(
                        EstadoCivil.id == persona.id_estado_civil
                    )
                )
                estado_civil = res.scalar_one()
                res = await async_db_session.execute(
                    select(Nacionalidad).where(
                        Nacionalidad.id == persona.id_nacionalidad
                    )
                )
                nac = res.scalar_one()
                nacionalidad = NacionalidadSchema(**nac.__dict__)

                direccion = await ServicioDireccionDomicilio.buscar_por_id_persona(persona.identificacion)
                contacto_emergencia = await ServicioContactoEmergencia.buscar_por_id_persona(persona.identificacion)

                res = await async_db_session.execute(select(InformacionBancaria).filter_by(id_persona=persona.identificacion))
                info_ban = res.all()
                cuenta_bancaria = InformacionBancariaSchema(
                    id=info_ban[0][0].id,
                    institucion_financiera= info_ban[0][0].institucion_financiera,
                    tipo_cuenta = TipoCuenta[info_ban[0][0].tipo_cuenta.value],
                    numero_cuenta = info_ban[0][0].numero_cuenta )   if info_ban else None
                results = await async_db_session.execute(
                    select(ExpedienteLaboral).filter_by(
                        id_persona=persona.identificacion
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
                    pais_origen=PaisSchema(**pais.__dict__),
                    estado_civil=EstadoCivilSchema(**estado_civil.__dict__),
                    discapacidad=DiscapacidadSchema(
                        **discapacidad.__dict__),
                    carnet_conadis=persona.carnet_conadis,
                    porcentaje_discapacidad=persona.porcentaje_discapacidad,
                    etnia=EtniaSchema(**etnia.__dict__),
                    nacionalidad=nacionalidad,
                    correo_institucional=persona.correo_institucional,
                    correo_personal=persona.correo_personal,
                    telefono_domicilio=persona.telefono_domicilio,
                    telefono_movil=persona.telefono_movil,
                    direccion_domicilio=direccion,
                    contacto_emergencia=contacto_emergencia,
                    informacion_bancaria=cuenta_bancaria,
                    tipo_sangre=persona.tipo_sangre,
                    licencia_conduccion=persona.lincencia_conduccion,
                    tipo_licencia=TipoLicenciaConduccion[
                        persona.tipo_licencia_conduccion.value] if persona.tipo_licencia_conduccion is not None else None,
                    fecha_ingreso=expediente.registrado_en


                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return informacion_personal

    @classmethod
    async def agregar_registro(cls, persona: InformacionPersonalPostSchema) -> bool:
        regsitrado: bool = False
        try:
            async_db_session = AsyncDatabaseSession()
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
            informacion_personal.lincencia_conduccion = persona.licencia_conduccion
            if persona.tipo_licencia:
                informacion_personal.tipo_licencia_conduccion = persona.tipo_licencia
            informacion_personal.direccion_domicilio = DireccionDomicilio(
                id_canton=persona.direccion_domicilio.id_canton,
                id_provincia=persona.direccion_domicilio.id_provincia,
                parroquia=persona.direccion_domicilio.parroquia,
                calle1=persona.direccion_domicilio.calle1,
                calle2=persona.direccion_domicilio.calle2,
                referencia=persona.direccion_domicilio.referencia)
            informacion_personal.contacto_emergencia = ContactoEmergencia(
                apellidos=persona.contacto_emergencia.apellidos,
                nombres=persona.contacto_emergencia.nombres,
                direccion=persona.contacto_emergencia.direccion,
                telefono_domicilio=persona.contacto_emergencia.telefono_domicilio,
                telefono_movil=persona.contacto_emergencia.telefono_movil
            )
            informacion_personal.informacion_bancaria = InformacionBancaria(
                institucion_financiera=persona.informacion_bancaria.institucion_financiera,
                tipo_cuenta=persona.informacion_bancaria.tipo_cuenta,
                numero_cuenta=persona.informacion_bancaria.numero_cuenta
            )
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
    async def actualizar_registro(cls, persona: InformacionPersonalPutSchema, id: str) -> bool:
        resp: bool = False
        try:
            async_db_session = AsyncDatabaseSession()
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

            results1 = await async_db_session.execute(
                select(ContactoEmergencia).filter_by(id_persona=id)
            )
            res = results1.all()
            if res:
                contacto_emergencia = res[0][0]
            else:
                contacto_emergencia = ContactoEmergencia()
            contacto_emergencia.apellidos = persona.contacto_emergencia.apellidos
            contacto_emergencia.nombres = persona.contacto_emergencia.nombres
            contacto_emergencia.direccion = persona.contacto_emergencia.direccion
            contacto_emergencia.telefono_movil = persona.contacto_emergencia.telefono_movil
            contacto_emergencia.telefono_domicilio = persona.contacto_emergencia.telefono_domicilio

            results1 = await async_db_session.execute(
                select(InformacionBancaria).filter_by(id_persona=id)
            )
            res = results1.all()
            informacion_bancaria = res[0][0] if res else InformacionBancaria()
            informacion_bancaria.institucion_financiera = persona.informacion_bancaria.institucion_financiera
            informacion_bancaria.tipo_cuenta = persona.informacion_bancaria.tipo_cuenta
            informacion_bancaria.numero_cuenta = persona.informacion_bancaria.numero_cuenta
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
            informacion_personal.telefono_domicilio = persona.telefono_domicilio if persona.telefono_domicilio is None else '0000000000'
            informacion_personal.tipo_sangre = persona.tipo_sangre
            informacion_personal.lincencia_conduccion = persona.licencia_conduccion
            if persona.tipo_licencia:
                informacion_personal.tipo_licencia_conduccion = persona.tipo_licencia
            informacion_personal.direccion_domicilio = direccion
            informacion_personal.contacto_emergencia = contacto_emergencia
            informacion_personal.informacion_bancaria = informacion_bancaria
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
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            query = delete(DireccionDomicilio).where(
                DireccionDomicilio.id_persona == id)
            await async_db_session.execute(query)
            query = delete(ContactoEmergencia).where(
                ContactoEmergencia.id_persona == id)
            await async_db_session.execute(query)
            query = delete(ExpedienteLaboral).where(
                ExpedienteLaboral.id_persona == id)
            await async_db_session.execute(query)

            query = delete(InformacionPersonal).where(
                InformacionPersonal.identificacion == id)
            await async_db_session.execute(query)

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
            async_db_session = AsyncDatabaseSession()
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
