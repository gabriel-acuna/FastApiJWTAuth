import pytest
from httpx import AsyncClient
from app.api.routes import app
from decouple import config


@pytest.fixture(scope="function")
async def test_app():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        token :str = None
        resp = await ac.post("/login", json={
            'email': config('ADMIN_EMAIL'),
            'password': config('ADMIN_PASS')
        })
        if resp.status_code == 200:
            r =resp.json()
            token = r['token']
          
        yield ac,  {"Authorization": f"Bearer {token}"}
