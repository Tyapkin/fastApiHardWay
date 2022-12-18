from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.core.config import settings
# from backend.apis.general_pages.route_homepage import general_page_router
from backend.api.base import api_router


def include_router(_app):
    _app.include_router(api_router)


def configure_static(_app):
    _app.mount('/static', StaticFiles(directory='backend/static'), name='static')


def start_application():
    _app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(_app)
    configure_static(_app)
    return _app


app = start_application()
