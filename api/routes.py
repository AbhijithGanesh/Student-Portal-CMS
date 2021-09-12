from django.shortcuts import render
from typing import *
from pydantic import BaseModel
from fastapi import APIRouter, Request
from pydantic.types import Json


class Table(BaseModel):
    Name:str
    Class:str
    Age:int
    
student_router = APIRouter()



@student_router.get("/api-endpoint-1")
def ReturnAll():
    return {"TestData":"Has been returned"}

