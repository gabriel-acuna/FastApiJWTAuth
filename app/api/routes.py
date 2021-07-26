from fastapi import  APIRouter, FastAPI
from app.api.endpoints import auth
api_router = APIRouter()

@api_router.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message":"Api test"}

api_router.include_router( auth.router, tags=["auth"])




app = FastAPI()
app.include_router(api_router)