from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def UserAccounts(request):
    if request.method == "GET":
        return render(request, 'user_accounts.html')
    elif request.method == "POST":
        return HttpResponse("POST User Accounts")


def CaAccounts(request):
    if request.method == "GET":
        return render(request, 'ca_accounts.html')
    elif request.method == "POST":
        return HttpResponse("POST CA Accounts")
