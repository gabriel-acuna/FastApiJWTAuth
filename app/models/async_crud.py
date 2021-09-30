from typing import Any, NoReturn
from sqlalchemy import update as sqlalchemy_update, insert
from sqlalchemy.sql.expression import delete, select
from app.database.conf import AsyncDatabaseSession


class OperacionesEscrituraAsinconas:
    @classmethod
    async def crear(cls, **kwargs) -> bool:
        ok: bool = False
        try:

            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            query = insert(cls).values(kwargs)
            await async_db_session.execute(query)
            await async_db_session.commit()
            ok = True
        except Exception as ex:
            raise

        finally:
            await async_db_session.close()
        return ok

    @classmethod
    async def actualizar(cls, id, **kwargs) -> bool:
        ok: bool = False
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            query = (
                sqlalchemy_update(cls)
                .where(cls.id == id)
                .values(**kwargs)
                .execution_options(synchronize_session="fetch")
            )

            await async_db_session.execute(query)
            await async_db_session.commit()
            ok = True
        except Exception as ex:
            raise
        finally:
            await async_db_session.close()
        return ok

class OperacionesLecturaAsincronas:
    @classmethod
    async def listar(cls):
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            query = select(cls)
            results = await async_db_session.execute(query)
            return results.all()
        except Exception as ex:
            raise
        finally:
            await async_db_session.close()

    @classmethod
    async def filtarPor(cls, **kwargs):
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            query = select(cls).filter_by(**kwargs)
            results = await async_db_session.execute(query)
            return results.all()
        except Exception as ex:
            raise
        finally:
            await async_db_session.close()

    @classmethod
    async def obtener(cls, id):
        try:

            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            query = select(cls).where(cls.id == id)
            results = await async_db_session.execute(query)
            return results.first()

        except Exception as ex:
            raise
        finally:
            await async_db_session.close()


class EliminacionAsincrona():
    @classmethod
    async def eliminar(cls, id: Any) -> bool:
        ok:bool = False
        try:
            async_db_session = AsyncDatabaseSession()
            await async_db_session.init()
            query = delete(cls).where(cls.id ==id)
            await async_db_session.execute(query)
            await async_db_session.commit()
            ok = True
        except Exception as ex:
            raise
        finally:
            await async_db_session.close()
        return ok