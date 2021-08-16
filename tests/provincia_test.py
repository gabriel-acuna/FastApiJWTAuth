from typing import List
import pytest
from httpx import AsyncClient
from app.api.routes import app
from decouple import config
from app.schemas.core.CantonSchema import CantonSchema


@pytest.mark.asyncio
async def test_listar_provincias():
    print('listar cantones')
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp =  await ac.get("/provincias")
        assert resp.status_code == 200
        assert len(resp.json()) > 0
        
     

@pytest.mark.asyncio
async def test_obtner_provincia():
    async with AsyncClient(app=app, base_url="http://test1") as ac:
        resp =  await ac.get("/provincias/1")
        assert resp.status_code == 200
        assert resp.json() == {"id":1,"provincia":"AZUAY","registrado_en":"2021-08-10T11:02:49.604761","actualizado_en":"2021-08-10T11:02:49.604761"}
        
@pytest.mark.asyncio
async def test_obtner_canton_con_status_code_404():
    async with AsyncClient(app=app, base_url="http://test2") as ac:
        resp =  await ac.get("/provincias/1000")
        assert resp.status_code == 404
        assert resp.json() == {'detail': 'Provincia no encontrada'}
        



