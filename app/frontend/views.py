from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return authenticated_home(request)
    return render(request, 'home.html')


def authenticated_home(request):
    return render(request, 'home.html')
