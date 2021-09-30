from django.shortcuts import render
from typing import *
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from pydantic.types import Json
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from .models import EventsProcessor, StudentProfile
from asgiref.sync import sync_to_async


class Table(BaseModel):
    Name: str
    Class: str
    Age: int


student_router = APIRouter()
security = HTTPBasic()


@student_router.get("/api-endpoint-1")
def Open_Dummy_Function():
    return {"TestData": "Has been returned"}


@student_router.get("/security-me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}


@student_router.get("/events-all")
def return_all_events():
    data = EventsProcessor()
    return data


@student_router.get("/data/{param_id}")
def get_by_id(param_id):
    data = list(
        StudentProfile.objects.filter(Application_Numebr=param_id)
    )  # API routing with Django ORM
    return data


@student_router.post("/data/POST")
def create_item(item):
    item = dict(item)
    m = StudentProfile(**item)
    m.save()
    return {"Message": "The Data has been added to the Model"}


@student_router.delete("/data/{UniqID}")
def delete_item(UniqID: str):
    data = StudentProfile.objects.filter(UniqueID=UniqID)
    return {"The following data will be deleted": list(data)}
    data.delete()


@student_router.put("/data/PUT/")
def put_item(Params: Table):
    item = dict(Params)
    m = StudentProfile(**item)
    m.save()
    return {"Message": "The Data has been added to the Model"}
