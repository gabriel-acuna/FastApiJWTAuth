from app.services.dac.ServicioHorasPorPerido import *

def test_listado_horas_periodo():
    listado = ServicioHorasPorPerido.verificar_datos_sga(7)
    assert len(listado)>0
    print(len(listado))