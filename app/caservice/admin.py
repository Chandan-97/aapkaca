from django.contrib import admin
from .models import CaService, CaServicesPrice, ServiceInterest

# Register your models here.

admin.site.register(CaService)
admin.site.register(CaServicesPrice)
admin.site.register(ServiceInterest)