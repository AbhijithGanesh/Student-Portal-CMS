import os
from django.apps import apps
from django.core.wsgi import get_wsgi_application
from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StudentCMS.settings')
apps.populate(settings.INSTALLED_APPS)

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware
from api.routes import student_router as router
from api.auth_user_router import LoginRouter

def get_application():
    """
    routes = [
        Mount("/static", app=StaticFiles(directory='static'), name = 'static'),
        Mount("/", WSGIMiddleware(get_wsgi_application())),
    ]
    These routes can be mounted as an array if you compromise on static files
    """
    app = FastAPI(title = settings.PROJECT_NAME, debug = settings.DEBUG, redoc_url="/inner-docs")
    app.include_router(router, prefix = "/api")
    app.include_router(LoginRouter, prefix="/security")
    app.mount("/static", app=StaticFiles(directory='static'), name = 'static')
    app.mount("/", WSGIMiddleware(get_wsgi_application()))
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = get_application()
