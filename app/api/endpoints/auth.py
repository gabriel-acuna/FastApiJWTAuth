from app.schemas.auth.TokenSchema import TokenSchema
from fastapi import APIRouter, Body, Response, status
from app.schemas.auth.UserLoginSchema import UserLoginSchema
from app.api.auth.auth_handler import signJWT
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
async def user_login(response: Response, user: UserLoginSchema = Body(...)):
    usuario = await ServicioLogin.verificar_usuario(credenciales=user)
    if usuario:
        print(usuario.__dict__)
        data_usuario = {
            'nombre': usuario.primer_nombre,
            'apellido': usuario.primer_apellido,
            'email': usuario.email,
            'roles': [rol.name for rol in usuario.roles]

        }

        token = signJWT(data_usuario)
        token_auth = {
            'tipo_token': TipoToken.acceso.name,
            'token': token,
            'usuario_id': usuario.id
        }
        print(token_auth)
        return TokenSchema(token=token, type=TipoToken.acceso.name)
    response.status_code = status.HTTP_400_BAD_REQUEST
    return MessageSchema(type="error", content="Credenciales incorecctas, la clave o el usuario no son correctos")
    ''' if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }'''
