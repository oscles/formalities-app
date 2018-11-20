from django.contrib import admin

# Register your models here.
from ..civil_servant.models import CivilServant

admin.site.register(CivilServant)