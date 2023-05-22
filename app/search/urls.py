from django.contrib import admin
from django.urls import path
from .views import CaServiceSearchList

urlpatterns = [
    path('ca_service', view=CaServiceSearchList, name='api_search_ca_service'),
]
