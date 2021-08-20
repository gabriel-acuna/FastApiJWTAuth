import pytest


@pytest.mark.asyncio
async def test_listar_cantones(test_app):
    resp = await test_app[0].get("/cantones")
    assert resp.status_code == 200
    assert len(resp.json()) > 0


@pytest.mark.asyncio
async def test_obtener_canton(test_app):
    resp = await test_app[0].get("/cantones/1")
    assert resp.status_code == 200
    canton = resp.json()
    assert canton['id'] == 1
    assert canton['canton'] == "CUENCA"


@pytest.mark.asyncio
async def test_obtener_canton_con_status_code_404(test_app):
    resp = await test_app[0].get("/cantones/1000")
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'Cantón no encontrado'}


@pytest.mark.asyncio
async def test_obtener_canton_con_status_code_442(test_app):
    resp = await test_app[0].get("/cantones/ghg")
    assert resp.status_code == 422
    r = resp.json()
    assert r['detail'][0]['type'] == 'type_error.integer'
