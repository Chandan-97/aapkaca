from django.contrib import admin
from django.urls import path, include
from .views import login_user, logout_user, login_ca, logout_ca, register_user, register_ca
urlpatterns = [
    path('user/login', login_user),
    path('user/logout', logout_user),
    path('ca/login', login_ca),
    path('ca/logout', logout_ca),
    path('user/register', register_user),
    path('ca/register', register_ca)
]