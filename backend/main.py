from fastapi import FastAPI
from backend.core.config import settings
from backend.apis.general_pages.route_homepage import general_page_router


def include_router(_app):
    _app.include_router(general_page_router)


def start_application():
    _app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(_app)
    return _app


app = start_application()
