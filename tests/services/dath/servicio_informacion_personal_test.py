from _pytest.mark import param
from app.schemas.core.DiscapacidadSchema import DiscapacidadPostSchema
from app.models.core.modelos_principales import Discapacidad, EstadoCivil, Etnia
from datetime import date
from app.schemas.dath.InformacionPersonalSchema import InformacionPersonalPostSchema, Sexo, TipoIdentificacion
from app.schemas.dath.DireccionSchema import DireccionPostSchema
from app.services.core.ServicioDiscapacidad import ServicioDiscapacidad
from app.services.core.ServicioEstadoCivil import ServicioEstadoCivil
from app.services.core.ServicioEtnia import ServicioEtnia
from app.services.dath.ServicioInformacionPersonal import *
import pytest
from app.schemas.dath import *
from app.models.dath.modelos import InformacionPersonal, DireccionDomicilio
from decouple import config


@pytest.mark.asyncio
async def test_agregar_registro():

    direccion = DireccionPostSchema(
        id_provincia=12,
        id_canton=139,
        parroquia='SAN LORENZO',
        calle1='CHIMBORAZO',
        calle2='FEBRES COREDERO',
        referencia='S/N'
    )

    estado_civil_existe = await ServicioEstadoCivil.existe(EstadoCivil(estado_civil='SOLTERO/A'))
    if not estado_civil_existe:
        await ServicioEstadoCivil.agregar_registro(EstadoCivil(estado_civil='SOLTERO/A'))
    estado_civil = await EstadoCivil.filtarPor(estado_civil='SOLTERO/A')

    discapacidad = Discapacidad(discapacidad='NINGUNA')
    existe = await ServicioDiscapacidad.existe(discapacidad)
    if not existe:
        ServicioDiscapacidad.agregar_registro(discapacidad)
    d = await Discapacidad.filtarPor(discapacidad='NINGUNA')

    existe_etnia = await ServicioEtnia.existe(Etnia(etnia='MONTUBIO/A'))
    if not existe_etnia:
        await ServicioEtnia.agregar_registro(Etnia(etnia='MONTUBIO/A'))
    etnia = await Etnia.filtarPor(etnia='MONTUBIO/A')

    # parametro para el método agregar_registro
    data = InformacionPersonalPostSchema(
        tipo_identificacion=TipoIdentificacion.CEDULA,
        identificacion=1314056407,
        primer_nombre='Gabriel',
        segundo_nombre='Stefano',
        primer_apellido='Acuña',
        segundo_apellido='Regalado',
        sexo=Sexo.HOMBRE,
        fecha_nacimiento=date(1993, 9, 27),
        pais_origen=68,
        estado_civil=estado_civil[0][0].id,
        discapacidad=d[0][0].id,
        porcentaje_discapacidad=0,
        etnia=etnia[0][0].id,
        correo_institucional=config('ADMIN_EMAIL'),
        correo_personal=config('EMAIL'),
        telefono_movil='+593985910098',
        direccion_domicilio=direccion,
        tipo_sangre='O+'

    )
    params = {'id': data.identificacion,
              'correo_institucional': data.correo_institucional}
    persona_existe = await ServicioInformacionPersonal.existe(**params
                                                        )
    # elimina el registro en caso que exista para evitar que falle el test
    print( 'exite',persona_existe)
    if persona_existe:
        await ServicioInformacionPersonal.eliminar_registro(
            data.identificacion
        )
    registrado = await ServicioInformacionPersonal.agregar_registro(persona=data)
    assert registrado == True

''''
@pytest.mark.asyncio
async def test_actualizar_registro():

    direccion = DireccionPostSchema(
        id_provincia=12,
        id_canton=139,
        parroquia='SAN LORENZO',
        calle1='CHIMBORAZO',
        calle2='FEBRES CORDERO',
        referencia='S/N'
    )

    estado_civil_existe = await ServicioEstadoCivil.existe(EstadoCivil(estado_civil='SOLTERO/A'))
    if not estado_civil_existe:
        await ServicioEstadoCivil.agregar_registro(EstadoCivil(estado_civil='SOLTERO/A'))
    estado_civil = await EstadoCivil.filtarPor(estado_civil='SOLTERO/A')

    discapacidad = Discapacidad(discapacidad='NINGUNA')
    existe = await ServicioDiscapacidad.existe(discapacidad)
    if not existe:
        ServicioDiscapacidad.agregar_registro(discapacidad)
    d = await Discapacidad.filtarPor(discapacidad='NINGUNA')

    existe_etnia = await ServicioEtnia.existe(Etnia(etnia='MONTUBIO/A'))
    if not existe_etnia:
        await ServicioEtnia.agregar_registro(Etnia(etnia='MONTUBIO/A'))
    etnia = await Etnia.filtarPor(etnia='MONTUBIO/A')

    # parametro para el método actualizar_registro
    data = InformacionPersonalPutSchema(
        tipo_identificacion=TipoIdentificacion.CEDULA,
        primer_nombre='Gabriel',
        segundo_nombre='Stefano',
        primer_apellido='Acuña',
        segundo_apellido='Regalado',
        sexo=Sexo.HOMBRE,
        fecha_nacimiento=date(1993, 9, 27),
        pais_origen=68,
        estado_civil=estado_civil[0][0].id,
        discapacidad=d[0][0].id,
        porcentaje_discapacidad=0,
        etnia=etnia[0][0].id,
        correo_institucional=config('ADMIN_EMAIL'),
        correo_personal=config('EMAIL'),
        telefono_movil='+593985910098',
        direccion_domicilio=direccion,
        tipo_sangre='O+'

    )
    actualizado = await ServicioInformacionPersonal.actualizar_registro(persona=data, id='1314056407')
    print('---test2-----', actualizado)

    assert actualizado ==True


@pytest.mark.asyncio
async def test_buscar_por_id():
    persona = await ServicioInformacionPersonal.buscar_por_id(id='1314056407')
    print(persona)'''
