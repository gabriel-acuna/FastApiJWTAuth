from app.schemas.dath.InformacionReproductivaSchema import *
from app.models.dath.modelos import InformacionReproductiva
from typing import List
import logging


class ServicioInformacionReproductiva():

    @classmethod
    async def listar_por_persona(cls, id_persona: str) -> List[InformacionReproductivaSchema]:
        lista: List[InformacionReproductivaSchema] = []
        try:
            filas = await InformacionReproductiva.filtarPor(id_persona=id_persona)
            for fila in filas:
                lista.append(InformacionReproductivaSchema(**fila[0].__dict__))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return lista

    @classmethod
    async def buscar_por_id(cls, id: str) -> InformacionReproductivaSchema:
        item: InformacionReproductivaSchema = None
        try:
            resultado = await InformacionReproductiva.obtener(id)
            if resultado:
                item = InformacionReproductivaSchema(
                    id = resultado[0].id,
                    id_persona = resultado[0].id_persona,
                    estado = resultado[0].estado,
                    incio = resultado[0].inicio,
                    fin = resultado[0].fin
                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

        return item

    @classmethod
    async def agregar_registro(cls, registro: InformacionReproductivaPostSchema) -> bool:
        try:
            return await InformacionReproductiva.crear(
                id_persona = registro.id_persona,
                estado = registro.estado,
                incio = registro.inicio,
                fin = registro.fin
            )
        
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
    
    @classmethod
    async def actualizar_registro(cls, registro: InformacionReproductivaPutSchema) -> bool:
        try:
            return await InformacionReproductiva.actualizar(
                id = registro.id,
                estado = registro.estado,
                incio = registro.incio,
                fin = registro.fin
            )
        
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await InformacionReproductiva.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)


    @classmethod
    async def existe (cls, registro: InformacionReproductivaPostSchema)-> bool:
        try:
            existe = await InformacionReproductiva.filtarPor(
                id_persona = registro.id_persona,
                estado = registro.estado,
                inicio = registro.incio
            )
            return True if existe else False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
