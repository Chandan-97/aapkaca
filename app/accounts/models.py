from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=14)


class UserCa(UserProfile):
    membership_number = models.CharField(max_length=7)
    state = models.CharField(max_length=30)
    address = models.CharField(max_length=120, blank=True)
    years_of_experience = models.IntegerField()
    degrees = models.CharField(max_length=120)
    profile_summary = models.CharField(max_length=250)
    business_services = models.CharField(max_length=250)
    ca_passing_year = models.DateField()
    worked_with_companies = models.CharField(max_length=250)
    awards_certifications = models.CharField(max_length=250)
    schedule = models.CharField(max_length=250)
    profile_picture = models.ImageField(upload_to='uploads/')
