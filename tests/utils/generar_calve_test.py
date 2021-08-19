import typing

import pytest
from app.utils.generar_clave import generar_calve

@pytest.mark.asyncio
async def test_generar_clave():
    clave = await generar_calve()
    assert len(clave) >= 8 and len(clave) <=16
    print(clave)