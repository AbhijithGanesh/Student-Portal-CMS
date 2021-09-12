from django.shortcuts import render
from django.http import HttpResponse    

def BackEnd_Logic(request):
    return HttpResponse("Hello World from Backend")

def LoginPage(request):
    if request.user.is_authenticated():
        return True
    