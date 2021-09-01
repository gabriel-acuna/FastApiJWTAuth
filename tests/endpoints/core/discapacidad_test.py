import pytest

@pytest.mark.asyncio
async def test_registrar_discapacidad_valores_numericos(test_app):
    resp = await test_app[0].post(url='/api/discapacidades', json={'discapacidad': 2884848},  headers= test_app[1])
    assert resp.status_code == 422
    assert resp.json() == {'detail': [{'loc': ['body', 'discapacidad'], 'msg': 'No debe contener números', 'type': 'value_error'}]}


@pytest.mark.asyncio
async def test_registrar_discapacidad_valores_numericos_con_espacios(test_app):
    resp = await test_app[0].post(url='/api/discapacidades', json={'discapacidad':' 2884848 '},  headers= test_app[1])
    assert resp.status_code == 422
    assert resp.json() == {'detail': [{'loc': ['body', 'discapacidad'], 'msg': 'No debe contener números', 'type': 'value_error'}]}


@pytest.mark.asyncio
async def test_registrar_discapacidad_espacios(test_app):
    resp = await test_app[0].post(url='/api/discapacidades', json={'discapacidad': '         '},  headers= test_app[1])
    assert resp.status_code == 422
    assert resp.json() == {'detail': [{'loc': ['body', 'discapacidad'], 'msg': 'No debe ser una cadena vacía o espacios', 'type': 'value_error'}]}


@pytest.mark.asyncio
async def test_registrar_discapacidad_menor_a_longitud_minima(test_app):
    resp = await test_app[0].post(url='/api/discapacidades', json={'discapacidad': 'test'},  headers= test_app[1])
    assert resp.status_code == 422
    assert resp.json() ==  {'detail': [{'loc': ['body', 'discapacidad'], 'msg': 'Longitud mínima 5 caracteres', 'type': 'value_error'}]} 


@pytest.mark.asyncio
async def test_registrar_discapacidad_menor_a_longitud_máxima(test_app):
    resp = await test_app[0].post(url='/api/discapacidades', 
        json={'discapacidad': 'ucboqsc cpsjqcjqspcpisqhc  ojcosjcoja qpisj    ahjpi   axajxa  hxia    jxi ji xaixjo   akxoa   xhapi   oajxa   oxxjaox oxjaj   x oa    xja xo  aiiiiiiiii'},
        headers= test_app[1])
    assert resp.status_code == 422
    assert resp.json() ==  {'detail': [{'loc': ['body', 'discapacidad'], 'msg': 'Longitud máxima 30 caracteres', 'type': 'value_error'}]} 

"""""
@pytest.mark.asyncio
async def test_registar_discapacidad_con_status_code_201(test_app):
    discapacidad = {'discapacidad':'FISICA MOTORA'}
    resp = await test_app[0].post(url='/api/discapacidades', json= discapacidad)
    assert resp.status_code == 201
    assert resp.json()=={'type':'success', 'content':'Registro exitoso'}


@pytest.mark.asyncio
async def test_registar_discapacidad_con_status_code_202(test_app):
    discapacidad = {'discapacidad':'FISICA MOTORA'}
    resp = await test_app[0].post(url='/api/discapacidades', json= discapacidad)
    assert resp.status_code == 202
    assert resp.json()=={'type':'warning', 'content':f'La discapacidad {discapacidad.discapacidad} ya está resgistrada'}

@pytest.mark.asyncio
async def test_listar_discapacidades(test_app):
    resp = await test_app[0].get(url='/api/discapacidades')
    assert resp.status_code == 200
    discapacidades = resp.json()
    assert len(discapacidades) > 0 """
    


