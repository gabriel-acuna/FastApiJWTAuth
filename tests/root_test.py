import pytest
from decouple import config
import socket


@pytest.mark.asyncio
async def test_root(test_app):
    resp =  await test_app.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"ies":"UNIVERSIDAD ESTATAL DEL SUR DE MANABÍ",
        "codigo_ies":1025,
        "provincia":"MANABÍ",
        "canton":"JIPIJAPA",
        "url":"http://unesum.edu.ec/",
        "documentacion_api":f"http://{socket.gethostname()}:{config('PORT')}/redoc"}
