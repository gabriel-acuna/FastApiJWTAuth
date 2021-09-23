import logging
from app.schemas.core.CantonSchema import CantonSchema
from app.schemas.core.ProvinciaSchema import ProvinciaSchema
from app.schemas.dath.DireccionSchema import DireccionSchema
from app.models.dath.modelos import DireccionDomicilio
from app.models.core.modelos_principales import  Provincia, Canton


class ServicioDireccionDomicilio():

    @classmethod
    async def buscar_por_id_persona(cls, id_perona: str) -> DireccionSchema:
        direccion: DireccionSchema = None
        try:
            dir = await DireccionDomicilio.filtarPor(id_persona=id_perona)
            if dir:
                provincia = await Provincia.obtener(dir[0][0].id_provincia)
                canton =  await Canton.obtener(dir[0][0].id_canton)
                direccion = DireccionSchema(
                    id = dir[0][0].id,
                    provincia = ProvinciaSchema(**provincia[0].__dict__),
                    canton = CantonSchema(**canton[0].__dict__),
                    parroquia = dir[0][0].parroquia,
                    calle1 = dir[0][0].calle1,
                    calle2 = dir[0][0].calle2,
                    referencia = dir[0][0].referencia

                )
        except Exception as ex:
            logging.error(f"Ha ocurrido una excepción {ex}", exc_info=True)
        return direccion
