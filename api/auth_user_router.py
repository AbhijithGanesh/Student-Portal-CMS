from fastapi import FastAPI, Request
from typing import *
from pydantic import BaseModel
from fastapi import APIRouter, Request
from pydantic.types import Json
from django.contrib.auth import authenticate


LoginRouter = APIRouter()


@LoginRouter.get('/')
def LoginForm(data,request: Request):
    userName = request.data.get("username")
    Password = request.data.get("password")
    try:
        authenticate(userName, Password)
    except ValueError:
        return -1

    
