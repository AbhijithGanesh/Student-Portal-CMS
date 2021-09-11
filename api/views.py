from django.shortcuts import render
from typing import *
from pydantic import BaseModel
from fastapi import APIRouter, Request
from pydantic.types import Json

router = APIRouter()

class Table(BaseModel):
    Name:str
    Class:str
    Age:int


@router.get("/api-endpoint-1")
def ReturnAll():
    return {"Key":"Value"}