import logging
from typing import List
from app.models.core.modelos_principales import TipoFuncionario
from app.schemas.core.TipoFuncionarioSchema import *


class ServicioTipoFuncionario():

    @classmethod
    async def listar(cls) -> List[TipoFuncionarioSchema]:
        esclafones: List[TipoFuncionarioSchema] = []
        try:
            filas = await TipoFuncionario.listar()
            for fila in filas:
                esclafones.append(TipoFuncionarioSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return esclafones

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await TipoFuncionario.obtener(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def agregar_registro(cls, tipo_funcionario: TipoFuncionarioPostSchema):
        try:
            return await TipoFuncionario.crear(tipo=tipo_funcionario.tipo)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, tipo_funcionario: TipoFuncionarioPutSchema):
        try:
            return await TipoFuncionario.actualizar(id=str(tipo_funcionario.id), tipo=tipo_funcionario.tipo)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await TipoFuncionario.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, tipo_funcionario: TipoFuncionario) -> bool:
        try:
            existe = await TipoFuncionario.filtarPor(tipo=tipo_funcionario.tipo)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
