import pytest

@pytest.mark.asyncio
async def test_listar_provincias(test_app):
    resp = await test_app[0].get("/api/provincias",  headers= test_app[1])
    assert resp.status_code == 200
    assert len(resp.json()) > 0


@pytest.mark.asyncio
async def test_obtener_provincia(test_app):
    resp = await test_app[0].get("/api/provincias/1",  headers= test_app[1])
    assert resp.status_code == 200
    provincia = resp.json()
    assert provincia['id'] == 1
    assert provincia['provincia'] == "AZUAY"


@pytest.mark.asyncio
async def test_obtener_provincia_con_status_code_404(test_app):
    resp = await test_app[0].get("/api/provincias/1000",  headers= test_app[1])
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'Provincia no encontrada'}


@pytest.mark.asyncio
async def test_obtener_cantones_provincia(test_app):
    resp = await test_app[0].get("/api/provincias/1/cantones",  headers= test_app[1])
    assert resp.status_code == 200
    assert len(resp.json()) > 0


@pytest.mark.asyncio
async def test_obtener_cantones_provincia_con_status_code_404(test_app):
    resp = await test_app[0].get("/api/provincias/1000/cantones",  headers= test_app[1])
    assert resp.status_code == 404
    assert resp.json() == {
        'detail': 'La provincia no se encontró o no tiene cantones registrados'}


@pytest.mark.asyncio
async def test_obtener_provincia_con_status_code_442(test_app):
    resp = await test_app[0].get("/api/provincias/vuyviyv",  headers= test_app[1])
    assert resp.status_code == 422
    r = resp.json()
    assert r['detail'][0]['type'] == 'type_error.integer'


@pytest.mark.asyncio
async def test_obtener_cantones_provincia_con_status_code_442(test_app):
    resp = await test_app[0].get("/api/provincias/vuyviyv/cantones",  headers= test_app[1])
    assert resp.status_code == 422
    r = resp.json()
    assert r['detail'][0]['type'] == 'type_error.integer'


