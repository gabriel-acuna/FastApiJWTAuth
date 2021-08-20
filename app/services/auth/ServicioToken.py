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
    async def agregar_registro(**kwargs) -> bool:
        try:
            return await TokenAutorizacion.crear(
                tipo_token=kwargs['tipo_token'],
                token=kwargs['token'],
                usuario_id=kwargs['usuario_id']

            )
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    async def actualizar_registro(**kwargs) -> bool:
        try:
            token: TokenAutorizacion
            resp = await TokenAutorizacion.filtarPor(token=kwargs['token'])
            if resp:
                token = resp[0][0]
                token.estado = False
                token.usado_hasta = datetime.now(0)
                return await TokenAutorizacion.actualizar(
                    id=token.id, estado=token.estado, usado_hasta=token.usado_hasta)
        except Exception as ex:
            print(f"Ha ocurrido una excepción {ex}")

    @classmethod
    def firmar_token(cls, user:  Dict[str, Any]) -> Dict[str, str]:
        payload = {
            "user": user,
            "expires": time.time() + 600
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return token

    @classmethod
    def decodificar_token(cls, token: str) -> dict:
        try:
            decoded_token = jwt.decode(
                token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return decoded_token if decoded_token["expires"] >= time.time() else None
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
            if not self.verificar_jwt_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Invalid authorization code.")

    def verificar_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = ServicioToken.decodificar_token(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
