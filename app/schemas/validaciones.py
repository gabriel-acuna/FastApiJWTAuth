def longitud_maxima(longitud:int, value:str):
    if len(value) > longitud:
        raise ValueError(f"Longitud máxima {longitud} caracteres")
    return value
    