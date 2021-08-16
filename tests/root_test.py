import pytest
from httpx import AsyncClient
from app.api.routes import app
from decouple import config
import socket


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp =  await ac.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"ies":"UNIVERSIDAD ESTATAL DEL SUR DE MANABÍ",
        "codigo_ies":1025,
        "provincia":"MANABÍ",
        "canton":"JIPIJAPA",
        "url":"http://unesum.edu.ec/",
        "documentacion_api":f"http://{socket.gethostname()}:{config('PORT')}/redoc"}
