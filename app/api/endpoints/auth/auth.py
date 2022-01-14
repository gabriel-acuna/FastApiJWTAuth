from app.schemas.auth.TokenSchema import TokenSchema
from fastapi import APIRouter, Body, Response, status, HTTPException, Depends
from app.services.auth import ServicioToken
from app.schemas.auth.UserLoginSchema import UserLoginSchema
from app.schemas.auth.UserSchema import ChangePasswordSchema, UserPostSchema, UserPutSchema
from app.services.auth.ServicioUsuario import ServicioUsuario
from app.schemas.Message import MessageSchema
from app.models.auth.cuentas_usuarios import TipoToken
from app.api.messages import ERROR_MSG, PUT_WARNING_MSG

router = APIRouter()


@router.post("/account", response_model=MessageSchema, status_code=201, dependencies=[Depends(ServicioToken.JWTBearer())])
async def crear_cuenta(user: UserPostSchema = Body(...)):
    registrado = await ServicioUsuario.crear_cuenta(user)
    if not registrado:
        raise HTTPException(
            status_code=400, detail="No se pudo crear la cuenta")
    return MessageSchema(type='success', content="La cuenta se creo exitosamente")


@router.put("/account", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def actulizar_cuenta(response: Response, user: UserPutSchema = Body(...)):
    existe = await ServicioUsuario.buscar_por_id(user.id)
    if not existe:
        response.status_code = status.HTTP_202_ACCEPTED
        return MessageSchema(type="warning", content=PUT_WARNING_MSG)

    actualizado = await ServicioUsuario.actualizar_cuenta(user)
    if not actualizado:
        response.status_code = status.HTTP_409_CONFLICT
        return MessageSchema(type="error", content=ERROR_MSG)
    return MessageSchema(type='success', content="La cuenta se actualizó exitosamente")


@router.post("/login", response_model=TokenSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def acceso_usuario(user: UserLoginSchema = Body(...)):
    usuario = await ServicioUsuario.verificar_usuario(credenciales=user)
    if usuario and usuario.estado == True:
        calve_valida = await ServicioUsuario.verificar_clave(user.password, usuario.clave_encriptada)
        if calve_valida:
            roles = await ServicioUsuario.obtener_roles(id=usuario.id)

            data_usuario = {
                'nombre': usuario.primer_nombre,
                'apellido': usuario.primer_apellido,
                'email': usuario.email,
                'roles': roles
            }

            token = ServicioToken.ServicioToken.firmar_token(data_usuario)
            token_auth = {
                'tipo_token': TipoToken.acceso,
                'token': token,
                'usuario_id': usuario.id
            }
            token_almacenado = await ServicioToken.ServicioToken.agregar_registro(**token_auth)
            if token_almacenado:
                return TokenSchema(token=token, type=TipoToken.acceso.value)

    raise HTTPException(
        status_code=400, detail="Credenciales incorrectas, la clave o el usuario no son correctos")


@router.put("/change-password", response_model=MessageSchema, dependencies=[Depends(ServicioToken.JWTBearer())])
async def cambiar_clave(response: Response, data: ChangePasswordSchema = Body(...)):
    usuario = await ServicioUsuario.verificar_usuario(credenciales=data)
    if not usuario:
        response.status_code = status.HTTP_202_ACCEPTED
        return MessageSchema(type="warning", content="No se pudo actualizar la contraseña")

    clave_valida = await ServicioUsuario.verificar_clave(data.clave_actual, usuario.clave_encriptada)

    if not clave_valida:
        raise HTTPException(
            status_code=400, detail="La clave actual no coincide")

    if data.clave_actual == data.clave_nueva:
        raise HTTPException(
            status_code=400, detail="La nueva contraseña no debe ser igual a la contraseña actual")

    clave_cifrada = ServicioUsuario.cifrar_clave(data.clave_nueva)
    actualizada = await ServicioUsuario.cambiar_clave(usuario.id, clave_cifrada)
    if actualizada:
        return MessageSchema(type="success", content="Cambio de contraseña exitoso")
    response.status_code = status.HTTP_409_CONFLICT
    return MessageSchema(type="error", content=ERROR_MSG)
