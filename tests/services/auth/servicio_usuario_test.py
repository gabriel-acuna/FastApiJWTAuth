import pytest
from app.services.auth.ServicioUsuario import ServicioUsuario

@pytest.mark.asyncio
async def test_listar_usuarios():
    usuarios = await ServicioUsuario.listar_usuarios()
    print(usuarios)