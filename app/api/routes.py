from fastapi import APIRouter, FastAPI
from app.api.endpoints import auth
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

app = FastAPI(title="Sigac Unesum API", )

app.include_router(api_router)
