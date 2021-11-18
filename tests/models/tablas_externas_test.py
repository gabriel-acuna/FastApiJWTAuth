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

