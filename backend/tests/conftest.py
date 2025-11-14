from __future__ import annotations

import asyncio
import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

os.environ.setdefault("OSINT_SHIELD_DATABASE_URL", "sqlite+aiosqlite:///./test_osint.db")

from app.ingestion.sample_loader import load_sample_data
from app.main import app


@pytest.fixture(scope="session")
def event_loop() -> asyncio.AbstractEventLoop:  # type: ignore[override]
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def prepare_db(event_loop: asyncio.AbstractEventLoop):
    db_file = Path("test_osint.db")
    if db_file.exists():
        db_file.unlink()
    event_loop.run_until_complete(load_sample_data())
    yield
    if db_file.exists():
        db_file.unlink()


@pytest.fixture(scope="session")
def client(prepare_db):
    with TestClient(app) as test_client:
        yield test_client
