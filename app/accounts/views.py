from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserCa
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.


def UserAccounts(request):
    if request.method == "GET":
        return render(request, 'user_accounts.html')
    elif request.method == "POST":
        body = request.POST.dict()
        email = body.get("login_email", "")
        password = body.get("login_password", "")

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('frontend__home'))
        else:
            return HttpResponse("Wrong password")


def CaAccounts(request):
    if request.method == "GET":
        return render(request, 'ca_accounts.html')
    elif request.method == "POST":
        body = request.POST.dict()
        email = body.get("login_email", "")
        password = body.get("login_password", "")

        user = authenticate(username=email, password=password)

        # if user is not None:
        #     # user is ca
        #     try:
        #         UserCa.objects.get(userprofile_ptr=user.profile)
        #         login(request, user)
        #         return HttpResponseRedirect(reverse('frontend__home'))
        #     except:
        #         return HttpResponse("Invalid Email / Password")
        # else:
        #     return HttpResponse("wrong password")


def UserAccountsRegister(request):
    if request.method == "GET":
        return render(request, 'user_accounts.html')
    elif request.method == "POST":
        body = request.POST.dict()
        full_name = body.get("full_name")
        email = body.get("email")
        mobile = body.get("mobile")
        business_need = body.get("business_need")
        ca_location_preference = body.get("ca_location_preference")
        location = body.get('location')
        password_1 = body.get("password_1")
        password_2 = body.get("password_2")

        if None in [full_name, email, mobile, business_need, ca_location_preference, location, password_1, password_2]:
            return HttpResponse("Please complete the form")

        if password_1 != password_2:
            return HttpResponse("Password not matching")

        # check for same email
        if User.objects.filter(email=email).exists():
            return HttpResponse("User already exists")

        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=full_name,
            password=password_1
        )

        userprofile = UserProfile(user=user, mobile=mobile).save()

        return HttpResponseRedirect(reverse('frontend__home'))

    return HttpResponse("User Accounts Register")


def CaAccountsRegister(request):
    return HttpResponse("CA Accounts Register")


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('frontend__home'))
