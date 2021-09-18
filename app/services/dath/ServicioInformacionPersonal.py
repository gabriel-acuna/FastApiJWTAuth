from typing import List
from sqlalchemy.sql.elements import or_
from sqlalchemy.sql.expression import delete,select
from app.schemas.dath.InformacionPersonalSchema import *
from app.models.dath.modelos import InformacionPersonal, DireccionDomicilio
from app.database.conf import async_db_session
import uuid


class ServicioInformacionPersonal():

    @classmethod
    async def listar(cls) -> List[InformacionPersonalSchema]:
        personal_ies: List[InformacionPersonalSchema] = []
        try:
            filas = await InformacionPersonal.listar()
            for fila in filas:
                print(fila)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
        return filas

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            persona = await InformacionPersonal.filtarPor(identificacion=id)
            if persona:
                print(persona[0][0].__dict__)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

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
                informacion_personal.nacionalidad = persona.nacionalidad
            informacion_personal.id_discapacidad =  persona.discapacidad
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
                calle1 = persona.direccion_domicilio.calle1,
                calle2 = persona.direccion_domicilio.calle2,
                referencia=persona.direccion_domicilio.referencia)
            async_db_session.add(informacion_personal)
            await async_db_session.commit()
            regsitrado = True
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
        finally:
            await async_db_session.close()
        return regsitrado

    @classmethod
    async def actualizar_registro(cls, persona: InformacionPersonalPutSchema, id: str):
        resp = False
        try:
            await async_db_session.init()
            informacion_personal = InformacionPersonal()
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
                informacion_personal.nacionalidad = persona.nacionalidad
            else:
                informacion_personal.nacionalidad = None
            informacion_personal.id_discapacidad = persona.direccion_domicilio
            if persona.carnet_conadis:
                informacion_personal.carnet_conadis = persona.carnet_conadis
            informacion_personal.porcentaje_discapacidad = persona.carnet_conadis
            informacion_personal.correo_institucional = persona.correo_institucional
            informacion_personal.correo_personal = persona.correo_personal
            informacion_personal.telefono_domicilio = persona.telefono_domicilio
            informacion_personal.tipo_sangre = persona.tipo_sangre
            if persona.licencia_conduccion:
                informacion_personal.lincencia_conduccion = persona.licencia_conduccion
            informacion_personal.direccion_domicilio =  DireccionDomicilio(
                id_canton=persona.direccion_domicilio.id_canton,
                id_provincia=persona.direccion_domicilio.id_provincia,
                parroquia=persona.direccion_domicilio.parroquia,
                referencia=persona.direccion_domicilio.referencia)

            query = select(InformacionPersonal.primer_nombre,
                           InformacionPersonal.primer_apellido).where(InformacionPersonal.identificacion == id)
            actualizado = await async_db_session.execute(query)
            if actualizado:
                resp = True

        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
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
            query1 = delete(InformacionPersonal).where(
                InformacionPersonal.identificacion == id)
            await async_db_session.execute(query1)
            await async_db_session.commit()
            elminado = True
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
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
            print(f"Ha ocurrido una excepción {ex}")
        finally:
            await async_db_session.close()
