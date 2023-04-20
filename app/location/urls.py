from django.urls import path

from .views import list_location

urlpatterns = [
    path('list', list_location),
]