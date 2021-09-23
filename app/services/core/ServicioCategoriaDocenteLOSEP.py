import logging
from app.models.core.modelos_principales import CategoriaDocenteLOSEP
from app.schemas.core import CategoriaDocenteLOSEPSchema
from app.schemas.core.CategoriaDocenteLOSEPSchema import *
from typing import List


class ServicioCategoriaDocenteLOSEP():

    @classmethod
    async def listar(cls) -> List[CategoriaDocenteLOSEPSchema]:
        categorias: List[CategoriaDocenteLOSEPSchema] = []
        try:
            filas = await CategoriaDocenteLOSEP.listar()
            for fila in filas:
                categorias.append(
                    CategoriaDocenteLOSEPSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return categorias

    @classmethod
    async def buscar_por_id(cls, id: str):
        try:
            return await CategoriaDocenteLOSEP.obtener(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def agregar_registro(cls, categoria: CategoriaDocenteLOSEPPostSchema):
        try:
            return await CategoriaDocenteLOSEP.crear(categoria_docente=categoria.categoria_docente)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, categoria: CategoriaDocenteLOSEPPostSchema):
        try:
            return await CategoriaDocenteLOSEP.actualizar(id=str(categoria.id), categoria_docente=categoria.categoria_docente)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str):
        try:
            return await CategoriaDocenteLOSEP.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, categoria: CategoriaDocenteLOSEP) -> bool:
        try:
            existe = await CategoriaDocenteLOSEP.filtarPor(categoria_docente=categoria.categoria_docente)
            if existe:
                return True
            return False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
