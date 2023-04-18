from django.db import models
from django.contrib.auth.models import User
from services.constants import LOCATION_CHOICES

# Create your models here.


class UserClient(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="client_user")
    mobile = models.CharField(max_length=14)
    business_need = models.TextField()
    location = models.CharField(max_length=30, choices=LOCATION_CHOICES)
    ca_location_pref = models.CharField(
        max_length=30, choices=LOCATION_CHOICES)


class UserCa(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="ca_user")
    mobile = models.CharField(max_length=14)
    membership_number = models.CharField(max_length=7)
    location = models.CharField(max_length=30, choices=LOCATION_CHOICES)
    address = models.CharField(max_length=120, blank=True)
    years_of_experience = models.IntegerField()
    degrees = models.CharField(max_length=120)
    summary = models.CharField(max_length=250)
    ca_passing_year = models.DateField()
    past_companies = models.CharField(max_length=250)
    awards_certifications = models.CharField(max_length=250)

    schedule = models.CharField(max_length=250)
    profile_picture = models.ImageField(upload_to='uploads/')
