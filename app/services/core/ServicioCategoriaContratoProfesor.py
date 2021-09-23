import logging
from app.models.core.modelos_principales import CategoriaContratoProfesor
from app.schemas.core import CategoriaContratoProfesorSchema
from app.schemas.core.CategoriaContratoProfesorSchema import *
from typing import List


class ServicioCategoriaContratoProfesor():

    @classmethod
    async def listar(cls) -> List[CategoriaContratoProfesorSchema]:
        categorias: List[CategoriaContratoProfesorSchema] = []
        try:
            filas = await CategoriaContratoProfesor.listar()
            for fila in filas:
                categorias.append(
                    CategoriaContratoProfesorSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return categorias

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await CategoriaContratoProfesor.obtener(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def agregar_registro(cls, categoria: CategoriaContratoProfesorPostSchema):
        try:
            return await CategoriaContratoProfesor.crear(categoria_contrato=categoria.categoria_contrato)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, categoria: CategoriaContratoProfesorPutSchema):
        try:
            return await CategoriaContratoProfesor.actualizar(id=str(categoria.id), categoria_contrato=categoria.categoria_contrato)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await CategoriaContratoProfesor.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, categoria: CategoriaContratoProfesor) -> bool:
        try:
            existe = await CategoriaContratoProfesor.filtarPor(categoria_contrato=categoria.categoria_contrato)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
