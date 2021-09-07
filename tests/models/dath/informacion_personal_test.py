import  pytest
from app.models.dath.modelos import *
from datetime import date

@pytest.mark.asyncio
async def test_crear_instancia():
    datos_personales = InformacionPersonal()
    assert isinstance(datos_personales, InformacionPersonal)


@pytest.mark.asyncio
async def test_calcular_edad():
    datos_personales = InformacionPersonal()
    assert isinstance(datos_personales, InformacionPersonal)
    datos_personales.fecha_nacimiento = date(1993,9,27)
    edad = datos_personales.calcular_edad()
    assert edad['años'] == 27