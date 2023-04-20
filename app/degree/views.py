import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from degree.models import DEGREE


@csrf_exempt
def list_degree(request):
    json_degree = json.dumps(DEGREE)
    return HttpResponse(json_degree)
