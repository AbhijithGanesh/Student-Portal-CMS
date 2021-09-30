from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def LandingPage(request):
    return render(request, "frontend/index.html")
