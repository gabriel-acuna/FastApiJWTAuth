from typing import List
import pytest
from httpx import AsyncClient
from app.api.routes import app
from decouple import config
from app.schemas.core.CantonSchema import CantonSchema


@pytest.mark.asyncio
async def test_listar_cantones():
    print('listar cantones')
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp =  await ac.get("/cantones")
        assert resp.status_code == 200
        assert len(resp.json()) > 0
        
     

@pytest.mark.asyncio
async def test_obtner_canton():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp =  await ac.get("/cantones/1")
        assert resp.status_code == 200
        assert resp.json() == {"id":1,"canton":"CUENCA","provincia_id":"1"}
        
@pytest.mark.asyncio
async def test_obtner_canton_con_status_code_404():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp =  await ac.get("/cantones/1000")
        assert resp.status_code == 404
        assert resp.json() == {'detail': 'Cantón no encontrado'}
        



