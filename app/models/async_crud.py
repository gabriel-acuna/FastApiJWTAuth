from typing import Any
from sqlalchemy import update as sqlalchemy_update
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
    async def listar(cls, id):
        query = select(cls)
        results = await async_db_session.execute(query)
        return results@classmethod

    @classmethod
    async def filtarPor(cls, **kwargs):
        query = cls.filter_by(kwargs)
        results = await async_db_session.execute(query)
        return results

    @classmethod
    async def obtner(cls, id):
        query = select(cls).where(cls.id == id)
        results = await async_db_session.execute(query)
        (result,) = results.one()
        return result


class EliminacionAsincrona():
    @classmethod
    async def eliminar(cls, objeto: Any):
        result = await async_db_session.delete(objeto)
        return result
