from django.contrib import admin
from django.urls import path, include
from .views import login_user, logout_user
urlpatterns = [
    path('user/login', login_user),
    path('user/logout', logout_user)
]