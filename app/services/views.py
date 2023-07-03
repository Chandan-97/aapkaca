from django.shortcuts import render
from .models import Services
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def list_services(request):
	services = Services.objects.all()
	services = list(services.values())
	context = dict()
	context["services"] = services
	return render(request, 'services_list.html', context)