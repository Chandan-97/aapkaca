import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, UserProfile, CAProfile, LOCATIONS, DEGREE


# Create your views here.

@csrf_exempt
def login_user(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    email = data.get("email")
    password = data.get("password")

    if None in [email, password]:
        return HttpResponse("email or password empty")

    user = authenticate(username=email, password=password)

    if user is None:
        return HttpResponse("Invalid email or password")

    if not user.is_user:
        return HttpResponse("Is not a user")
    login(request, user)
    return HttpResponse("Logged In")


@csrf_exempt
def logout_user(request):
    logout(request)
    return HttpResponse("Logged Out")


@csrf_exempt
def login_ca(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    email = data.get("email")
    password = data.get("password")

    if None in [email, password]:
        return HttpResponse("email or password empty")

    user = authenticate(username=email, password=password)

    if user is None:
        return HttpResponse("Invalid email or password")

    if not user.ca:
        return HttpResponse("Is not a CA")
    login(request, user)
    return HttpResponse("Logged In")


@csrf_exempt
def logout_ca(request):
    logout(request)
    return HttpResponse("Logged Out")


@csrf_exempt
def register_user(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

    full_name = data.get('full_name')
    phone_no = data.get('phone_no')
    email = data.get('email')
    business_need = data.get('business_need')
    location_pref = data.get('location_pref')
    location = data.get('location')
    password = data.get('password1')

    if None in [full_name, phone_no, email, password]:
        return HttpResponse("full name, phone no, email and password mandatory")

    if password and password != data.get('password2'):
        return HttpResponse('password mismatch')

    user = User.objects.create_user(username=email, email=email, password=password, phone_no=phone_no,
                                    full_name=full_name, is_user=True)

    user_profile = UserProfile(user=user, business_need=business_need, location_pref=location_pref, location=location)
    user_profile.save()
    return HttpResponse("User created")


@csrf_exempt
def register_ca(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

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

    if None in [full_name, phone_no, email, password, location, years_of_experience, degrees, summary, passout_year]:
        return HttpResponse("full name, phone no, email, password, location, years_of_experience, degrees, "
                            "summary and passout_year mandatory")

    if password and password != data.get('password2'):
        return HttpResponse('password mismatch')

    user = User.objects.create_user(username=email, email=email, password=password, phone_no=phone_no,
                                    full_name=full_name, is_user=True)

    ca_profile = CAProfile(user=user, location=location, office_address=office_address, years_of_experience=years_of_experience, degrees=degrees, summary=summary, passout_year=passout_year)
    ca_profile.save()
    return HttpResponse("CA created")
