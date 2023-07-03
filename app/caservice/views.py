import json

from django.shortcuts import render
from .models import CaService, CaServicesPrice
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def list_caservices(request):
	services = CaService.objects.all()
	services = list(services.values())
	return JsonResponse(services, safe=False)

from .models import CaServicePriceV2
from services.models import Services
from useraccounts.models import User
from django.forms.models import model_to_dict

def list_caserevicesv2(request):
	services = CaServicePriceV2.objects.all()
	services = list(services.values())
	for service in services:
		service["service"] = model_to_dict(Services.objects.get(id=service["service_id"]), fields=["id", "title"])
		service["ca"] = model_to_dict(User.objects.get(id=service["ca_id"]), fields=["id", "username", "email"])
	context = dict()
	context["services"] = services
	return render(request, 'ca_services_list.html', context)


@csrf_exempt
def list_caservicesprice(request):
	# ca = request.user
	services_prices = list(CaServicesPrice.objects.all())
	return JsonResponse(services_prices, safe=False)


@csrf_exempt
@login_required
def set_caservicesprice(request):
	body_unicode = request.body.decode('utf-8')
	data = json.loads(body_unicode)

	error_msg = ""
	for d in data:
		service_id = d.get('service_id')
		price = d.get('price')

		if None in [service_id, price]:
			error_msg += "\n Put service_id and price"
			continue

		obj = CaServicesPrice.objects.filter(ca=request.user, service__id=service_id)
		if obj:
			obj[0].price = price
			obj[0].save()
		else:
			CaServicesPrice(service__id=service_id, ca=request.user, price=price).save()
			obj = CaServicesPrice.objects.filter(ca=request.user, service__id=service_id)
			obj[0].price = price
			obj[0].save()

	if error_msg:
		return HttpResponse(error_msg)
	return HttpResponse("Saved successfully")
