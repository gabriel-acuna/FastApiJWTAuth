from decouple import config
import socket
from app.schemas.InfoIES import InfoIESSchema
from fastapi import APIRouter, FastAPI
from app.api.endpoints.auth import auth
import app.api.endpoints.core as core
from starlette.middleware.cors import CORSMiddleware


api_router = APIRouter()

api_router.include_router(auth.router, tags=["Auth"])
api_router.include_router(core.pais.router, tags=["Países"])
api_router.include_router(core.provincia.router, tags=["Provincias"])
api_router.include_router(core.canton.router, tags=["Cantones"])
api_router.include_router(core.discapacidad.router, tags=["Discapacidades"])
api_router.include_router(core.etnia.router, tags=["Etnias"])
api_router.include_router(core.nacionalidad.router, tags=["Nacionalidades"])
api_router.include_router(core.tipo_documento.router, tags=["Tipo documento"])
api_router.include_router(core.relacion_ies.router, tags=["Relación IES"])
api_router.include_router(core.tipo_escalafon_nombramiento.router, tags=[
                          "Tipo escalafón nombramiento"])
api_router.include_router(core.categoria_contrato_profesor.router, tags=[
                          "Categoría contrato profesor"])
api_router.include_router(core.tiempo_dedicacion_profesor.router, tags=[
                          "Tiempo dedicación profesor"])
api_router.include_router(core.nivel_educativo.router, tags=["Nivel educativo"])
api_router.include_router(core.tipo_funcionario.router, tags=["Tipo funcionario"])
api_router.include_router(core.tipo_docente_loes.router, tags=["Tipo docente LOES"])
api_router.include_router(core.categoria_docente_losep.router, tags=[
                          "Categoría docente LOSEP"])

app = FastAPI(title="SIGAC UNESUM API",
              description='''REST APi para el Sistema de Gestión de Aseguramiento
                    de la Calidad de la Universidad Estatal del Sur de Manabí''')
                    
@app.get("/", tags=["root"], response_model=InfoIESSchema)
async def info_ies() -> dict:
    return InfoIESSchema(
        ies="UNIVERSIDAD ESTATAL DEL SUR DE MANABÍ",
        codigo_ies=1025,
        provincia="MANABÍ",
        canton="JIPIJAPA",
        url="http://unesum.edu.ec/",
        documentacion_api=f"http://{socket.gethostname()}:{config('PORT')}/redoc")



# CORS
if config('BACKEND_CORS_ORIGINS'):
        
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[origin for origin in config('BACKEND_CORS_ORIGINS').split()],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix='/api')