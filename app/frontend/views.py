import json

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
from rest_framework import status

from caservice.models import CaService
from useraccounts.models import User, CAProfile, UserProfile


def home(request):
    if request.user.is_authenticated:
        if request.user.is_ca:
            return render(request, "home.html")
        if request.user.is_user:
            return render(request, "home.html")
    return render(request, 'home.html')


def ca_login(request):
    if request.method == "GET":
        return render(request, 'ca_login.html')
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        password = data.get("password")

        if email:
            email = email.strip()
        if password:
            password = password.strip()

        if None in [email, password] or len(email) == 0 or len(password) == 0:
            messages.error(request, 'Email or Password Empty')
            return render(request, 'ca_login.html')

        user = authenticate(username=email, password=password)

        if user is None:
            messages.error(request, 'Invalid email or password')
            return render(request, 'ca_login.html')

        if not user.is_ca:
            messages.success(request, 'User not registered as CA')
            return render(request, 'ca_login.html')
        login(request, user)
        messages.success(request, "Logged In")
        return redirect('frontend__home')


def ca_register(request):
    if request.method == "GET":
        return render(request, 'ca_register.html')
    if request.method == "POST":
        data = request.POST

        full_name = data.get('full_name')
        phone_no = data.get('phone_no')
        email = data.get('email')
        location = data.get('location')
        office_address = data.get('office_address')
        years_of_experience = data.get('years_of_experience')
        degrees = data.get('degrees')
        summary = data.get('summary')
        passout_year = data.get('passout_year')
        password = data.get('password1')

        if None in [full_name, phone_no, email, password, location, years_of_experience, degrees, summary,
                    passout_year]:
            messages.error(request, "full name, phone no, email, password, location, years_of_experience, degrees, "
                                    "summary and passout_year mandatory")
            return render(request, 'ca_register.html')

        if password and password != data.get('password2'):
            messages.error(request, 'password mismatch')
            return render(request, 'ca_register.html')

        if not isinstance(degrees, list):
            degrees = [degrees]

        user = User.objects.create_user(username=email, email=email, password=password, phone_no=phone_no,
                                        full_name=full_name, is_ca=True)

        ca_profile = CAProfile(user=user, location=location, office_address=office_address,
                               years_of_experience=years_of_experience, degrees=degrees, summary=summary,
                               passout_year=passout_year)
        ca_profile.save()
        messages.success(request, "Successfully Registered")
        return redirect('frontend__ca_login')


def ca_logout(request):
    logout(request)
    return redirect("frontend__home")


def user_login(request):
    if request.method == "GET":
        return render(request, 'user_login.html')
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        password = data.get("password")

        if email:
            email = email.strip()
        if password:
            password = password.strip()

        if None in [email, password] or len(email) == 0 or len(password) == 0:
            messages.error(request, 'Email or Password Empty')
            return render(request, 'user_login.html')

        user = authenticate(username=email, password=password)

        if user is None:
            messages.error(request, 'Invalid email or password')
            return render(request, 'user_login.html')

        if not user.is_user:
            messages.success(request, 'User registered as CA')
            return render(request, 'user_login.html')
        login(request, user)
        messages.success(request, "Logged In")
        return redirect('frontend__home')


def user_register(request):
    if request.method == "GET":
        return render(request, 'user_register.html')
    if request.method == "POST":
        data = request.POST

        full_name = data.get('full_name')
        phone_no = data.get('phone_no')
        email = data.get('email')
        business_need = data.get('business_need')
        location_pref = data.get('location_pref')
        location = data.get('location')
        password = data.get('password1')

        if None in [full_name, phone_no, email, password]:
            messages.error(request, "full name, phone no, email and password mandatory")
            return render(request, 'user_register.html')

        if password and password != data.get('password2'):
            messages.error(request, 'password mismatch')
            return render(request, 'user_register.html')

        if not isinstance(location_pref, list):
            location_pref = [location_pref]

        user = User.objects.create_user(username=email, email=email, password=password, phone_no=phone_no,
                                        full_name=full_name, is_user=True)

        user_profile = UserProfile(user=user, business_need=business_need, location_pref=location_pref,
                                   location=location)
        user_profile.save()
        messages.success(request, "Successfully Registered")
        return redirect("frontend__user_login")


def user_logout(request):
    logout(request)
    return redirect("frontend__home")


def authenticated_home(request):
    return render(request, 'home.html')


def services_list(request):
    services = CaService.objects.all()
    services = list(services.values())

    context = {
        "services": list()
    }
    for s in services:
        obj = {
            "title": s["title"],
            "features": s["features"]["list_show"]
        }
        context["services"].append(obj)

    return render(request, 'user_services_list.html', context)


def test(request):
    services = CaService.objects.all()
    services = list(services.values())

    context = {
        "services": list()
    }
    for s in services:
        obj = {
            "title": s["title"],
            "features": s["features"]["list_show"]
        }
        context["services"].append(obj)

    return render(request, 'user_services_list.html', context)
