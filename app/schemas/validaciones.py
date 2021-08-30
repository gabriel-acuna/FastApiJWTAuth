import re

from sqlalchemy.util.compat import raise_
def longitud_maxima(longitud:int, value:str, longitud_minima:int=3 ):
    if len(value) > longitud:
        raise ValueError(f"Longitud máxima {longitud} caracteres")
    if len(value) < longitud_minima:
        raise ValueError(f"Longitud mínima {longitud_minima} caracteres")
    if len(value.strip()) ==0:
        raise ValueError(f"No debe ser una cadena vacía o espacios")
    return value

def es_alafanumerico(value:str):
    res = re.search(r'^[A-Z]*\b.\d$', value)
    print(res)
    if not res:
        raise ValueError(f"Debe tener el siguiente formato ASDFGGH 2")

    return res
def es_no_numerico(value:str):
    value = value.strip()
    res = value.isnumeric()
    if res or not value.isalpha():
        raise ValueError(f"No debe contener números")
    return res

