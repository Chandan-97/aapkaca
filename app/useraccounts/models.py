from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
from degree.models import DEGREE
from location.models import LOCATIONS


class User(AbstractUser):
    is_ca = models.BooleanField('Is CA', default=False)
    is_user = models.BooleanField('Is User', default=False)
    phone_no = models.CharField(max_length=16, unique=True)
    full_name = models.CharField(max_length=32)


class UserProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='user_profile')
    business_need = models.TextField(max_length=256, null=True, blank=True)
    location_pref = MultiSelectField(choices=LOCATIONS, max_choices=3, max_length=64, null=True, blank=True)
    location = models.CharField(choices=LOCATIONS, max_length=16, null=True, blank=True)

    def __str__(self):
        return self.user.full_name


class CAProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='ca_profile')
    location = models.CharField(choices=LOCATIONS, max_length=16)
    office_address = models.CharField(max_length=128, null=True, blank=True)
    years_of_experience = models.IntegerField()
    degrees = MultiSelectField(choices=DEGREE, max_choices=5, max_length=128)
    summary = models.CharField(max_length=256)
    passout_year = models.IntegerField()

    def __str__(self):
        return self.user.full_name
