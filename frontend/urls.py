from django.urls import path
from frontend.views import LandingPage


urlpatterns = [
    path("", LandingPage),
]
