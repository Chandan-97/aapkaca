from django.contrib import admin
from .models import CaService, CaServicesPrice

# Register your models here.

admin.site.register(CaService)
admin.site.register(CaServicesPrice)