from sqlalchemy.sql.expression import select
from app.models.foreign_tables import *
from app.services.dac.ServicioPeridoAcademico import *


def test_listado_periodos_academicos():
    listado = ServicioPeriodoAcademico.listar()
    assert len(listado)>0
    print(listado)
    print(len(listado))