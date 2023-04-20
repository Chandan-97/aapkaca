from django.urls import path

from .views import list_degree

urlpatterns = [
    path('list', list_degree),
]