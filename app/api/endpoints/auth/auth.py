from app.schemas.auth.TokenSchema import TokenSchema
from fastapi import APIRouter, Body, Response, status, HTTPException
from app.schemas.auth.UserLoginSchema import UserLoginSchema
from app.services.auth.ServicioLogin import ServicioLogin
from app.services.auth.ServicioToken import ServicioToken
from app.schemas.Message import MessageSchema
from app.models.auth.cuentas_usuarios import TipoToken


router = APIRouter()


''''
@router.post("/signup")
async def create_user(user: UserSchema.UserPostSchema = Body(...)):
    users.append(user) 
    return signJWT(user.email)
'''


@router.post("/login", response_model=TokenSchema)
async def user_login(user: UserLoginSchema = Body(...)):
    usuario = await ServicioLogin.verificar_usuario(credenciales=user)
    if usuario and usuario.estado == True:
        calve_valida = await ServicioLogin.verificar_clave(user.password, usuario.clave_encriptada)
        if calve_valida:
            roles = await ServicioLogin.obtener_roles(id=usuario.id)

            data_usuario = {
                'nombre': usuario.primer_nombre,
                'apellido': usuario.primer_apellido,
                'email': usuario.email,
                'roles': roles
            }

            token = ServicioToken.firmar_token(data_usuario)
            token_auth = {
                'tipo_token': TipoToken.acceso,
                'token': token,
                'usuario_id': usuario.id
            }
            token_almacenado = await ServicioToken.agregar_registro(**token_auth)
            if token_almacenado:
                return TokenSchema(token=token, type=TipoToken.acceso.value)

    raise HTTPException(
        status_code=400, detail="Credenciales incorecctas, la clave o el usuario no son correctos")
