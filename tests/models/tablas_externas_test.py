from sqlalchemy.sql.expression import select
from app.models.foreign_tables import *
from app.services.dac.ServicioHorasPorPerido import *


def test_consultar_profesores():
    session = loadSession()
    results =  session.execute(
        select(Profesor)
    )
    listado = results.all()
    assert len(listado)>0
    print(listado[0][0].__dict__)

def test_consultar_periodo_academico():
    session = loadSession()
    results =  session.execute(
        select(PeriodoAcademico.inicio, PeriodoAcademico.fin).where(PeriodoAcademico.id==8)
    )
    periodo = results.all()
    print(periodo)

