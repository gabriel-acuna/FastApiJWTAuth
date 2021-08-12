from fastapi import APIRouter, FastAPI
from app.api.endpoints import auth, canton, discapacidad, etnia,nacionalidad, pais, provincia, tipo_documento, relacion_ies
api_router = APIRouter()


@api_router.get("/", tags=["root"])
async def read_root() -> dict:
    return {
        "IES": "UNIVERSIDAD ESTATAL DEL SUR DE MANABÍ",
        "CODIGO_IES":1025,
        "PROVINCIA":"MANABÍ",
        "CANTÓN":"JIPIJAPA",
        "URL":"http://unesum.edu.ec/"
        }

api_router.include_router(auth.router, tags=["Auth"])
api_router.include_router(pais.router, tags=["Países"])
api_router.include_router(provincia.router, tags=["Provincias"])
api_router.include_router(canton.router, tags= ["Cantones"])
api_router.include_router(discapacidad.router, tags=["Discapacidades"])
api_router.include_router(etnia.router, tags=["Etnias"])
api_router.include_router(nacionalidad.router, tags=["Nacionalidades"])
api_router.include_router(tipo_documento.router, tags=["Tipo documento"] )
api_router.include_router(relacion_ies.router, tags=["Relación IES"])

app = FastAPI(title="Sigac Unesum API", )

app.include_router(api_router)
