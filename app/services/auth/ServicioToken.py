from app.models.auth.cuentas_usuarios import TokenAutorizacion
from datetime import datetime
import time
from typing import Any, Dict
import jwt
from decouple import config
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


class ServicioToken():

    @classmethod
    async def agregar_registro(cls, **kwargs) -> bool:
        try:
            return await TokenAutorizacion.crear(
                tipo_token=kwargs['tipo_token'],
                token=kwargs['token'],
                usuario_id=kwargs['usuario_id']

            )
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def actualizar_registro(cls, token_id: str) -> bool:
        try:
            return await TokenAutorizacion.actualizar(
                id=token_id, estado=False, usado_hasta=datetime.now())
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    def firmar_token(cls, user:  Dict[str, Any]) -> Dict[str, str]:
        payload = {
            "user": user,
            "expires": time.time() + 300
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return token

    @classmethod
    async def decodificar_token(cls, token: str, token_id: str) -> dict:
        try:
            decoded_token = jwt.decode(
                token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            if decoded_token["expires"] >= time.time():
                return decoded_token
            else:
                await ServicioToken.actualizar_registro(token_id)
                return None
        except:
            return {}


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme.")
            token_valido = await self.verificar_jwt(credentials.credentials)
            if not token_valido:
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")

    async def verificar_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            token =  await TokenAutorizacion.filtarPor(token=jwtoken)
            if token and token[0][0].estado == True:
                payload = await ServicioToken.decodificar_token(jwtoken , token[0][0].id)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
