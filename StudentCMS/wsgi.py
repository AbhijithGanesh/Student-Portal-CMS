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
from api.views import router

def get_application():
    routes = [
        Mount("/static", app=StaticFiles(directory='static'), name = 'static'),
        Mount('/', WSGIMiddleware(get_wsgi_application()))
    ]
    app = FastAPI(title = settings.PROJECT_NAME, debug = settings.DEBUG,routes=routes)
    app.include_router(router, prefix = "/api")

    return app

app = get_application()
