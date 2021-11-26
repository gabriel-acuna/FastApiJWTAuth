from app.schemas.dath.FamiliarSchema import *
from app.models.dath.modelos import FamiliarPersonal
import logging
from typing import List


class ServicioFamiliarPersoal():

    @classmethod
    async def listar_por_id_persona(cls, id_persona: str) -> List[FamiliarSchema]:
        familiares: List[FamiliarSchema] = []
        try:
            filas = await FamiliarPersonal.filtarPor(id_persona=id_persona)
            for fila in filas:
                familiar: FamiliarPersonal = fila[0]
                familiares.append(FamiliarSchema(
                    id=familiar.id,
                    id_persona=familiar.id_persona,
                    parentesco=familiar.parentesco,
                    identificacion=familiar.identificacion,
                    nombres=familiar.nombres,
                    apellidos=familiar.apellidos,
                    sexo=familiar.sexo,
                    fecha_nacimiento=familiar.fecha_nacimiento,
                    edad=familiar.calcular_edad()

                ))
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return familiares

    @classmethod
    async def agregar_registro(cls, familiar: FamiliarPostSchema) -> bool:
        try:
            return await FamiliarPersonal.crear(
                id_persona=familiar.id_persona,
                parentesco=familiar.parentesco,
                identificacio=familiar.identificacion,
                nombres=familiar.nombres,
                apellidos=familiar.apellidos,
                sexo=familiar.sexo,
                fecha_nacimiento=familiar.fecha_nacimiento
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def actualizar_registro(cls, familiar: FamiliarPutSchema) -> bool:
        try:
            return await FamiliarPersonal.crear(
                id=familiar.id,
                parentesco=familiar.parentesco,
                identificacio=familiar.identificacion,
                nombres=familiar.nombres,
                apellidos=familiar.apellidos,
                sexo=familiar.sexo,
                fecha_nacimiento=familiar.fecha_nacimiento
            )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def eliminar_registro(cls, id: str) -> bool:
        try:
            return await FamiliarPersonal.eliminar(id)
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)

    @classmethod
    async def existe(cls, familiar: FamiliarPostSchema) -> bool:
        try:
            existe = await FamiliarPersonal.filtarPor(
                id_persona=familiar.id_persona,
                identificacion=familiar.identificacion
            )
            return True if existe else False
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
