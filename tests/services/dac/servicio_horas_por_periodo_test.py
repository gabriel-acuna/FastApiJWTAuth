from sqlalchemy.sql.expression import select
from app.models.foreign_tables import *
from app.services.dac.ServicioHorasPorPerido import *

def test_listado_horas_periodo():
    listado = ServicioHorasPorPerido.verificar_datos_sga(7)
    assert len(listado)>0
    print(len(listado))