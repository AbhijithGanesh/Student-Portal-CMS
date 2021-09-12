from django.db import models

from pytz import country_names as c
from datetime import date

dict_choices = dict(c)
_choices = []
_keys = list(dict_choices.keys())
_value = list(dict_choices.values())
if len(_keys) == len(_value):
    for i in range(len(_keys)):
        a = [_keys[i], _value[i]]
        _choices.append(tuple(a))


class StudentProfile(models.Model):
    Name = models.CharField(max_length=300)
    Application_Number = models.BigIntegerField()
    Date_Of_Birth = models.DateField()
    Gender = models.CharField(
        max_length=30,
        choices=[
            ("M", "Male"),
            ("F", "Female"),
            ("N", "Non-Binary"),
            ("W", "Would not like to reveal"),
        ],
    )
    HomeState = models.CharField(max_length=300)
    Country = models.CharField(max_length=75, choices=_choices)
    ContactNumber = models.BigIntegerField()

class ContactUs(models.Model):
    Department_Name = models.CharField(max_length=300)
    Department_Head = models.CharField(max_length=300)
    Department_ContactDetails = models.IntegerField()

    class Meta:
       verbose_name_plural = "Contact Us"
    
class Events(models.Model):
    Event_Name = models.CharField(max_length = 50)
    Event_Head = models.ForeignKey(StudentProfile, on_delete = models.DO_NOTHING)
    Event_Duration = models.DurationField()
    Event_Descripton = models.TextField(null = False, default = "Empty Description")

    class Meta:
       verbose_name_plural = "Events and Notices"
