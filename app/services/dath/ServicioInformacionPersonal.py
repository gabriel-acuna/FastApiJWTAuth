from typing import List
from app.schemas.dath.InformacionPersonalSchema import *
from app.models.dath.modelos import InformacionPersonal
from app.database.conf import async_db_session


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
    async def buscar_por_id(cls, id:str):
        pass


    @classmethod
    async def actualizar_registro(cls, persona: InformacionPersonalPostSchema):
        try:
           async_db_session.init()
           informacion_personal =  InformacionPersonal()
           persona.tipo_identificacion = persona.tipo_identificacion
           informacion_personal.identificacion = persona.identificacion
           informacion_personal.primer_nombre = persona.primer_nombre 
           informacion_personal.segundo_nombre = persona.segundo_nombre
           informacion_personal.primer_apellido = persona.primer_apellido
           informacion_personal.segundo_apellido = persona.segundo_apellido
           informacion_personal.sexo = persona.sexo
           informacion_personal.fecha_nacimiento = persona.fecha_nacimiento
           informacion_personal.id_pais_origen = persona.pais_origen
           informacion_personal.id_estado_civil =  persona.estado_civil
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
           informacion_personal.direccion_domicilio = persona.direccion_domicilio
           async_db_session.add(informacion_personal)
           async_db_session.commit()

        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")
        finally:
            async_db_session.close()

