import random
import string


async def generar_calve()-> str:
    '''
    ---------   Longitud de la contraseña ----------
        * longitud mínima: 8 caracteres
        * longitud máxima: 16 caracteres

    '''
    longitud = int(random.uniform(8, 17))

    letas = string.ascii_letters
    valores_numericos = string.digits
    simbolos = string.punctuation
    

    # combinación de valores
    combinacion = letas+valores_numericos + simbolos

    temp = random.sample(combinacion, longitud)

    # formar la contraseña
    password = "".join(temp)

    return password
