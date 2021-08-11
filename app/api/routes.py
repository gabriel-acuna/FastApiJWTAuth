from fastapi import APIRouter, FastAPI
from app.api.endpoints import auth, canton, discapacidad, etnia, nacionalidad, pais, provincia
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

api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(pais.router, tags=["paises"])
api_router.include_router(provincia.router, tags=["provincias"])
api_router.include_router(canton.router, tags= ["cantones"])
api_router.include_router(discapacidad.router, tags=["discapacidades"])
api_router.include_router(etnia.router, tags=["etnias"])
api_router.include_router(nacionalidad.router, tags=["nacionalidades"])

app = FastAPI(title="Sigac Unesum API", )

app.include_router(api_router)
