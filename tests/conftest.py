import pytest
from httpx import AsyncClient
from app.api.routes import app



@pytest.fixture(scope="function")
async def test_app():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac