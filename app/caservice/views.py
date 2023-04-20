from .models import CaService
from django.http import JsonResponse


# Create your views here.

def list_caservices(request):
	services = CaService.objects.all()
	services = list(services.values())
	return JsonResponse(services)


# def list_caservicesprice(request):
# 	ca = request.user
# 	services_prices = list(CaServicesPrice.objects.filter(ca=request.user))
# 	return JsonResponse(services_prices)


