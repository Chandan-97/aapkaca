from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from caservice.models import CaServicesPrice
from .models import CaServiceSearch


@csrf_exempt
def CaServiceSearchList(request, *args, **kwargs):
    body = request.POST.dict()
    query = body.get('query', "")
    results = CaServiceSearch.objects.filter(search_string__icontains=query)
    if not results:
        results = CaServicesPrice.objects.all()

    response = list()
    for r in results:
        response.append(
            {
                "id": r.ca.id,
                "name": r.ca.full_name,
                "location": r.ca.user_profile.location
            }
        )

    return JsonResponse(response, safe=False)
