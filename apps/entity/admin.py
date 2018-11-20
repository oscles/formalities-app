from django.contrib import admin

# Register your models here.
from ..entity.models import Entity

admin.site.register(Entity)
