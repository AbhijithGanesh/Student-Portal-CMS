from django.db import models
from pydantic import *
from typing import *
from django.contrib.auth.models import User
from CMSLogic.models import *
from asgiref.sync import sync_to_async


def EventsProcessor():
    Data = list(Events.objects.all())
    # Description = Data.get("Event_Descripton")
    # Event_Incharge = Data.get("Event_Incharge")
    return Data
