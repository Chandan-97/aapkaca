from django.contrib import admin
from django.urls import path
from .views import home, ca_login, ca_register, user_login, test, ca_logout, user_register, user_logout, services_list,\
    ca_dashboard, services_interest

urlpatterns = [
    path('', view=home, name='frontend__home'),
    path('ca_login', view=ca_login, name='frontend__ca_login'),
    path('ca_register', view=ca_register, name='frontend__ca_register'),
    path('ca_logout', view=ca_logout, name='frontend__ca_logout'),

    path('user_login', view=user_login, name='frontend__user_login'),
    path('user_register', view=user_register, name='frontend__user_register'),
    path('user_logout', view=user_logout, name='frontend__user_logout'),

    path('services', view=services_list, name='frontend__services_list'),
    path('ca_dashboard', view=ca_dashboard, name='frontend__ca_dashboard'),
    path('services/interest', view=services_interest, name='frontend__services_interest'),
    path('test', view=test, name='test')
]
