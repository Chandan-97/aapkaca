from django.urls import path

from .views import list_services

urlpatterns = [
    path('all', list_services)
]