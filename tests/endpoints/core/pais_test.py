import pytest


@pytest.mark.asyncio
async def test_listar_paises(test_app):
    cliente, token = test_app
    resp = await cliente.get('/paises', headers= token)
    assert resp.status_code == 200
    assert len(resp.json()) > 0

@pytest.mark.asyncio
async def test_obtener_pais(test_app):
    resp = await test_app[0].get('/paises/1', headers= test_app[1])
    assert resp.status_code == 200
    r = resp.json()
    assert type(r['id']) == int


@pytest.mark.asyncio
async def test_obtener_pais_con_status_code_404(test_app):
   
    resp = await test_app[0].get('/paises/1000', headers= test_app[1])
    assert resp.status_code == 404
    assert resp.json() == {'detail': 'País no encontrado'}

    
@pytest.mark.asyncio
async def test_obtener_pais_con_status_code_422(test_app):
    resp = await test_app[0].get('/paises/uji', headers = test_app[1])
    assert resp.status_code == 422
    r = resp.json()
    assert r['detail'][0]['type'] == 'type_error.integer'
