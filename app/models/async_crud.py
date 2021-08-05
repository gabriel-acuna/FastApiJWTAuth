from typing import Any, NoReturn
from sqlalchemy import update as sqlalchemy_update
import sqlalchemy
from sqlalchemy.sql.expression import select
from app.database.conf import async_db_session


class OperacionesEscrituraAsinconas:
    @classmethod
    async def crear(cls, **kwargs):
        async_db_session.add(cls, **kwargs)
        await async_db_session.commit()

    @classmethod
    async def actualizar(cls, id, **kwargs):
        query = (
            sqlalchemy_update(cls)
            .where(cls.id == id)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
        )

        await async_db_session.execute(query)
        await async_db_session.commit()


class OperacionesLecturaAsincronas:
    @classmethod
    async def listar(cls):
        try:
            await async_db_session.init()
            query = select(cls)
            results = await async_db_session.execute(query)
            return results.all()
        except Exception as ex:
            raise(f"Ha ocurrido una excepción: {ex}")
        finally:
            await async_db_session.close()

    @classmethod
    async def filtarPor(cls, **kwargs):
        try:
            await async_db_session.init()
            query = select(cls).filter_by(**kwargs)
            results = await async_db_session.execute(query)
            return results.all()
        except Exception as ex:
            print(f"Ha ocurrido una excepción: {ex}")
        finally:
            await async_db_session.close()

    @classmethod
    async def obtener(cls, id):
        try:
        
            await async_db_session.init()
            query = select(cls).where(cls.id == id)
            results = await async_db_session.execute(query)
            return results.first() 

        except Exception as ex:
            print(f"Ha ocurrido una excepción: {ex}")
        finally:
            await async_db_session.close()


class EliminacionAsincrona():
    @classmethod
    async def eliminar(cls, objeto: Any):
        await async_db_session.init()
        result = await async_db_session.delete(objeto)
        return result
