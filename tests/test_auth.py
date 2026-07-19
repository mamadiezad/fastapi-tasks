"""Tests for authentication endpoints."""

import pytest
from httpx import AsyncClient, ASGITransport


@pytest.mark.asyncio
async def test_register_user():
    """Test user registration."""
    from app.main import app

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/auth/register",
            json={
                "email": "test@example.com",
                "username": "testuser",
                "password": "StrongPass123!",
            },
        )
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert data["user"]["email"] == "test@example.com"
    assert data["user"]["username"] == "testuser"


@pytest.mark.asyncio
async def test_register_duplicate():
    """Test duplicate registration returns 409."""
    from app.main import app

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Register once
        await client.post(
            "/api/v1/auth/register",
            json={
                "email": "dup@example.com",
                "username": "duplicate",
                "password": "StrongPass123!",
            },
        )
        # Register again
        response = await client.post(
            "/api/v1/auth/register",
            json={
                "email": "dup@example.com",
                "username": "duplicate",
                "password": "StrongPass123!",
            },
        )
    assert response.status_code == 409


@pytest.mark.asyncio
async def test_login():
    """Test user login returns token."""
    from app.main import app

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Register first
        await client.post(
            "/api/v1/auth/register",
            json={
                "email": "login@example.com",
                "username": "loginuser",
                "password": "StrongPass123!",
            },
        )
        # Login
        response = await client.post(
            "/api/v1/auth/login",
            json={
                "email": "login@example.com",
                "password": "StrongPass123!",
            },
        )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_invalid():
    """Test login with wrong password returns 401."""
    from app.main import app

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/auth/login",
            json={
                "email": "nonexistent@example.com",
                "password": "wrongpass",
            },
        )
    assert response.status_code == 401
