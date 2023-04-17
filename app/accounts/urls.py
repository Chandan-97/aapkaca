from django.contrib import admin
from django.urls import path
from .views import UserAccounts, CaAccounts, UserAccountsRegister, CaAccountsRegister, LogoutView

urlpatterns = [
    path('user/register', view=UserAccountsRegister,
         name='accounts__user_register'),
    path('user', view=UserAccounts, name='accounts__user'),
    path('ca/register', view=CaAccountsRegister, name='accounts__ca_register'),
    path('ca', view=CaAccounts, name='accounts__ca'),
    path('logout', view=LogoutView, name='accounts__logout')
]
