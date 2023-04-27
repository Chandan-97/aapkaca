from django.contrib import admin
from django.urls import path, include
from .views import login_user, logout_user, login_ca, logout_ca, register_user, register_ca
urlpatterns = [
    path('user/login', login_user, name='useraccounts__user_login'),
    path('user/logout', logout_user, name='useraccounts__user_logout'),
    path('ca/login', login_ca, name='useraccounts__ca_login'),
    path('ca/logout', logout_ca, name='useraccounts__ca_logout'),
    path('user/register', register_user, name='useraccounts__user_register'),
    path('ca/register', register_ca, name='useraccounts__ca_register'),
]