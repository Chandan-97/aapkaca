import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from location.models import LOCATIONS


@csrf_exempt
def list_location(request):
    json_locations = json.dumps(LOCATIONS)
    return HttpResponse(json_locations)
