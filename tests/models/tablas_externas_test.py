from sqlalchemy.sql.expression import select
from app.models.foreign_tables import *


def test_consultar_profesores():
    session = loadSession()
    results =  session.execute(
        select(Persona.id, Persona.cedula, Persona.nombres).join(Persona.profesor)
    )
    listado = results.all()
    assert len(listado)>0
    print(listado)