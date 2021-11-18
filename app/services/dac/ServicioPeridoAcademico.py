from typing import Any, Dict, List

from sqlalchemy.sql.expression import asc
from app.models.foreign_tables import PeriodoAcademico, loadSession
from sqlalchemy import select, or_

from app.schemas.dac.PeriodoAcademicoSchema import PeriodoAcademicoSchema


class ServicioPeriodoAcademico():

    @classmethod
    def listar(cls) -> List[PeriodoAcademicoSchema]:
        listado_periodos:List[PeriodoAcademicoSchema] =[]
        session = loadSession()
        results = session.execute(
            select(
                PeriodoAcademico.id,
                PeriodoAcademico.nombre,
                PeriodoAcademico.inicio,
                PeriodoAcademico.fin,
                PeriodoAcademico.activo
            ).where(or_(PeriodoAcademico.nombre.startswith('P'), PeriodoAcademico.nombre.startswith('S')))
            .order_by(asc(PeriodoAcademico.inicio))
        )
        periodos = results.all()
        if periodos:
            for periodo in periodos:
                nombre: str = None
                if periodo[2].year == periodo[3].year:
                    nombre = f'PI {periodo[2].year}'
                else: 
                    nombre = f'PII {periodo[2].year}'
                listado_periodos.append(
                    PeriodoAcademicoSchema(
                        id = periodo[0],
                        nombre = nombre,
                        inicio = periodo[2],
                        fin = periodo[3],
                        activo = periodo[4]
                    )
                )
                
        return listado_periodos