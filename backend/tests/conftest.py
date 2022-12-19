import sys
import os
from typing import Any, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.db.base import Base
from backend.db.session import get_db
from backend.api.base import api_router
from backend.main import app

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


SQLALCHEMY_DATABASE_URL = 'sqlite:///test_db.db'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def start_application():
    app.include_router(api_router)
    return app


@pytest.fixture(scope='function')
def client() -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the 'db_session' fixture to overwrite
    the 'get_db' dependency that is injected into routes.
    """
    def _get_test_db():
        db = SessionTesting(bind=engine.connect())
        try:
            yield db
        finally:
            db.close()
    Base.metadata.create_all(engine)
    with TestClient(app) as client:
        app.dependency_overrides[get_db] = _get_test_db
        yield client
        app.dependency_overrides = {}
    Base.metadata.drop_all(engine)
