from .models import CaService, CaServicesPrice
from rest_framework import serializers

class CaServicesSerializer(serializers.ModelSerializer):
	class Meta: 
		model = CaService
		fields = ["title", "description"]


class CaServicesPriceSerializer(serializers.ModelSerializer):
	services = CaServicesSerializer(many=True, read_only=True)
	class Meta:
		model = CaServicesPrice
		fields = ["services", "price", "description"]