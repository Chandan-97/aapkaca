from django.urls import path

from .views import list_caservices

urlpatterns = [
    path('list', list_caservices),
]