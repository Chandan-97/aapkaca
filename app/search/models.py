from django.db import models

# Create your models here.
from useraccounts.models import User


class CaServiceSearch(models.Model):
    search_string = models.CharField(max_length=255)
    ca = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["search_string", "ca"]
        index_together = ["search_string", "ca"]
