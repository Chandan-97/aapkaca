from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.

LOCATIONS = (
    ('DELHI_NCR', 'Delhi NCR'),
    ('BHOPAL', 'Bhopal'),
    ('INDORE', 'Indore'),
    ('UP', 'Uttar Pradesh'),
    ('PUNJAB', 'Punjab'),
    ('RAJASTHAN', 'Rajasthan'),
)

DEGREE = (
    (1, 'B.Tech'),
    (2, 'B.Arch'),
    (3, 'BBA'),
    (4, 'BCA')
)


class User(AbstractUser):
    is_ca = models.BooleanField('Is CA', default=False)
    is_user = models.BooleanField('Is User', default=False)
    phone_no = models.CharField(max_length=16)
    full_name = models.CharField(max_length=32)


class UserProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='user_profile')
    business_need = models.TextField(max_length=256, null=True, blank=True)
    location_pref = MultiSelectField(choices=LOCATIONS, max_choices=3, max_length=64)
    location = models.CharField(choices=LOCATIONS, max_length=16)


class CAProfile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='ca_profile')
    location = models.CharField(choices=LOCATIONS, max_length=16)
    office_address = models.CharField(max_length=128)
    years_of_experience = models.IntegerField()
    degrees = MultiSelectField(choices=DEGREE, max_choices=5, max_length=128)
    summary = models.CharField(max_length=256)
    passout_year = models.IntegerField()
