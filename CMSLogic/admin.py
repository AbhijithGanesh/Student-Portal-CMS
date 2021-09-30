from django.contrib import admin
from .models import StudentProfile, Events, ContactUs


admin.site.register([StudentProfile, ContactUs, Events])
