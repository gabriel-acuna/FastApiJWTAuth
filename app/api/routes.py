from decouple import config
import socket
from app.schemas.InfoIES import InfoIESSchema
from fastapi import APIRouter, FastAPI
from app.api.endpoints import auth, canton, discapacidad, etnia, nacionalidad, tiempo_dedicacion_profesor
from app.api.endpoints import pais, provincia, tipo_documento, relacion_ies, tipo_escalafon_nombramiento
api_router = APIRouter()


@api_router.get("/", tags=["root"], response_model=InfoIESSchema)
async def info_ies() -> dict:
    return InfoIESSchema(
        ies="UNIVERSIDAD ESTATAL DEL SUR DE MANABÍ",
        codigo_ies=1025,
        provincia="MANABÍ",
        canton="JIPIJAPA",
        url="http://unesum.edu.ec/",
        documentacion_api=f"http://{socket.gethostname()}:{config('PORT')}/redoc")


api_router.include_router(auth.router, tags=["Auth"])
api_router.include_router(pais.router, tags=["Países"])
api_router.include_router(provincia.router, tags=["Provincias"])
api_router.include_router(canton.router, tags=["Cantones"])
api_router.include_router(discapacidad.router, tags=["Discapacidades"])
api_router.include_router(etnia.router, tags=["Etnias"])
api_router.include_router(nacionalidad.router, tags=["Nacionalidades"])
api_router.include_router(tipo_documento.router, tags=["Tipo documento"])
api_router.include_router(relacion_ies.router, tags=["Relación IES"])
api_router.include_router(tipo_escalafon_nombramiento.router, tags=[
                          "Tipo escalafón nombramiento"])
api_router.include_router(tipo_escalafon_nombramiento.router, tags=[
                          "Categoría contrato docente"])
api_router.include_router(tiempo_dedicacion_profesor.router, tags=[
                          "Tiempo dedicación profesor"])


app = FastAPI(title="Sigac Unesum API", )

app.include_router(api_router)
