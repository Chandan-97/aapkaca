import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
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
