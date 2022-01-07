from typing import Any, Dict, List
from app.models.foreign_tables import *
from sqlalchemy import and_
from decouple import config
class ServicioHorasPorPerido():

    @classmethod
    def verificar_datos_sga(cls, periodo_academico: int) -> List[Any]:
        listado_horas_periodo = []
        session = loadSession()
        results = session.execute(
            select(ProfesorDistributivoHoras).where(
                (ProfesorDistributivoHoras.periodo_id == periodo_academico) & 
                (ProfesorDistributivoHoras.coordinacion_id != 5) & (ProfesorDistributivoHoras.coordinacion_id !=6)))
        filas = results.all()
        for fila in filas:
            asignacion: ProfesorDistributivoHoras = fila[0]
            asignacion_profesor: Dict[str, Any] = {}
            res = session.execute(
                f'''select per.cedula, per.pasaporte,
                       per.nombres, per.apellido1, per.apellido2
                       from {config('SGA_DB_SCHEMA')}.sga_persona  per inner join
                       {config('SGA_DB_SCHEMA')}.sga_profesor pro on per.id = pro.persona_id where pro.id = {asignacion.profesor_id}''' )
                
            profesor = res.all()
            asignacion_profesor['periodo'] = periodo_academico
            asignacion_profesor["profesor"] = {
                'identificacion': {'cedula': profesor[0][0], 'pasaporte': profesor[0][1] },
                'apellido1': profesor[0][3],
                'apellido2': profesor[0][4],
                'nombres': profesor[0][2]
            }
            res = session.execute(
                f'''select dd.horas from {config('SGA_DB_SCHEMA')}.sga_detalledistributivo dd inner join  
                    {config('SGA_DB_SCHEMA')}.sga_criteriodocenciaperiodo  cdp on  dd.criteriodocenciaperiodo_id = cdp.id 
                    where dd.distributivo_id ={asignacion.id} and 
                    (cdp.criterio_id = 5 or cdp.criterio_id = 6 or cdp.criterio_id = 19)''')
            h_clase = res.all()
            if h_clase:
                asignacion_profesor['horas_calse'] = h_clase[0][0]
            else:
                asignacion_profesor['horas_calse'] = 0
            res = session.execute(
                f'''select dd.horas from {config('SGA_DB_SCHEMA')}.sga_detalledistributivo dd inner join  
                    {config('SGA_DB_SCHEMA')}.sga_criteriodocenciaperiodo  cdp on  dd.criteriodocenciaperiodo_id = cdp.id
                    where dd.distributivo_id ={asignacion.id} and cdp.criterio_id = 17''')
            h_tutorias = res.all()
            
            if h_tutorias:
                asignacion_profesor['horas_tutorias'] = h_tutorias[0][0]
            else: 
                asignacion_profesor['horas_tutorias'] = 0
            
            asignacion_profesor['horas_adminsitracion'] = float(asignacion.horasgestion)
            asignacion_profesor['horasinvestigacion'] = float(asignacion.horasinvestigacion)
            asignacion_profesor['horas_vinculacion'] = float(asignacion.horasvinculacion)
            asignacion_profesor['horas_otras_actividades'] = float(asignacion.horasotrasactividades)
            listado_horas_periodo.append(asignacion_profesor)
        return listado_horas_periodo
