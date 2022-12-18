from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='backend/templates')
general_page_router = APIRouter()


@general_page_router.get('/')
def home(request: Request):
    return templates.TemplateResponse(
        'general_pages/homepage.html',
        {'request': request}
    )
