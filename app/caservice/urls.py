from django.urls import path

from .views import list_caservices, list_caservicesprice, set_caservicesprice

urlpatterns = [
    path('all', list_caservices),
    path('allprice', list_caservicesprice),
    path('setprice', set_caservicesprice),
]