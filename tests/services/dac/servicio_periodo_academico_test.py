from app.services.dac.ServicioPeridoAcademico import ServicioPeriodoAcademico


def test_listado_periodos_academicos():
    listado = ServicioPeriodoAcademico.listar()
    assert len(listado)>0
    print(listado)
    print(len(listado))