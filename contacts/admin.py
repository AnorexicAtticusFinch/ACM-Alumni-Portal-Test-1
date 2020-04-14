from django.contrib import admin

# Register your models here.
from .models import AlumniContact, AlumniContactInterest

admin.site.register(AlumniContact)
admin.site.register(AlumniContactInterest)