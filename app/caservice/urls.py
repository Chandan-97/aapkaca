from django.urls import path

from .views import list_caservices, list_caservicesprice, set_caservicesprice, list_caserevicesv2

urlpatterns = [
    path('all', list_caservices),
    path('allprice', list_caservicesprice),
    path('setprice', set_caservicesprice),
    path('ca_services_price', list_caserevicesv2)
]