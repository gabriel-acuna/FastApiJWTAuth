import logging
from app.schemas.core.OrganigramaSchema import AreaOrganigrama
from typing import List

from sqlalchemy.sql.functions import mode
from app.models.core.modelos_principales import AreaInstitucion
from app.schemas.core.AreaInstitucionalSchema import *
from app.database.conf import AsyncDatabaseSession


class ServicioAreaInstitucion():

    @classmethod
    async def listar(cls) -> List[AreaInstitucionSchema]:
        areas: List[AreaInstitucion] = []
        try:
            filas = await AreaInstitucion.listar()
            for fila in filas:
                areas.append(AreaInstitucionSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return areas

    @classmethod
    async def buscar_por_id(cls, id: int):
        try:
            return await AreaInstitucion.obtener(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def agregar_registro(cls, area: AreaInstitucionalPostSchema):
        try:
            return await AreaInstitucion.crear(
                nombre=area.nombre,
                codigo=area.codigo
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, area: AreaInstitucionalPutSchema):
        try:
            return await AreaInstitucion.actualizar(
                id=area.id,
                nombre=area.nombre,
                codigo=area.codigo
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: int):
        try:
            return await AreaInstitucion.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def obtener_subareas(cls, parms: dict) -> AreaOrganigrama:
        area_institucion: AreaInstitucionSchema = None
        sub_areas: List[AreaInstitucionSchema] = []
        try:
            area = await AreaInstitucion.obtener(parms['id_area'])
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            if area:
                area_institucion = AreaInstitucion(
                    **area[0].__dict__
                )
                filas = await async_db_session.execute(
                    '''
                    select ai.* from public.areas_institucionales ai 
                    inner join public.organigrama o on o.id_sub_area = ai.id
                    where o.id_area_institucional =: id_area 
                    and o.id_estructura_institucional =: id_estructura
                    ''', **parms
                )

                for fila in filas:
                    sub_areas.append(
                        AreaInstitucion(
                            **area[0].__dict__
                        )
                    )
            return AreaOrganigrama(
                id_estructura=parms['id_estructura'],
                area = area_institucion,
                areas = sub_areas

            )
        except Exception as ex:
                logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
           await async_db_session.close()


    @classmethod
    async def existe(cls, area: AreaInstitucionSchema) -> bool:
        try:
            existe = await AreaInstitucionSchema.filtarPor(nombre=area.documento_aprobacion)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
