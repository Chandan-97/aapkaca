from django.contrib import admin
from django.urls import path
from .views import UserAccounts, CaAccounts

urlpatterns = [
    path('user', view=UserAccounts, name='accounts__user'),
    path('ca', view=CaAccounts, name='accounts__ca'),
]
