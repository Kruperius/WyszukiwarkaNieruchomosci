from django.contrib import admin

# Register your models here.
from .models import Nieruchomosci, Zrodla

admin.site.register(Nieruchomosci)
admin.site.register(Zrodla)