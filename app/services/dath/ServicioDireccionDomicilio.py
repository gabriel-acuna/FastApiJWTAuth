import logging

from sqlalchemy.sql.expression import select
from app.schemas.core.CantonSchema import CantonSchema
from app.schemas.core.ProvinciaSchema import ProvinciaSchema
from app.schemas.dath.DireccionSchema import DireccionSchema
from app.models.dath.modelos import DireccionDomicilio
from app.models.core.modelos_principales import Provincia, Canton
from app.database.conf import AsyncDatabaseSession


class ServicioDireccionDomicilio():

    @classmethod
    async def buscar_por_id_persona(cls, id_persona: str) -> DireccionSchema:
        direccion: DireccionSchema = None
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            res = await async_db_session.execute(
                select(DireccionDomicilio).where(
                    DireccionDomicilio.id_persona == id_persona
                )
            )
            dir = res.scalar_one()
            if dir:
                res = await async_db_session.execute(
                    select(
                        Provincia
                    ).where(Provincia.id == dir.id_provincia)
                )
                provincia = res.scalar_one()
                res = await async_db_session.execute(
                    select(
                        Canton
                    ).where(Canton.id == dir.id_canton)
                )
                canton = res.scalar_one()
                direccion = DireccionSchema(
                    id=dir.id,
                    provincia=ProvinciaSchema(**provincia.__dict__),
                    canton=CantonSchema(**canton.__dict__),
                    parroquia=dir.parroquia,
                    calle1=dir.calle1,
                    calle2=dir.calle2,
                    referencia=dir.referencia

                )

        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        finally:
            await async_db_session.close()
        return direccion
