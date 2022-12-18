from fastapi import APIRouter

from backend.api.v1 import route_general_pages
from backend.api.v1 import route_users


api_router = APIRouter()
api_router.include_router(
    route_general_pages.general_page_router,
    prefix='',
    tags=['general_pages']
)
api_router.include_router(
    route_users.router,
    prefix='/users',
    tags=['users']
)
