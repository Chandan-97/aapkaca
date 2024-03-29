from django.db import models

from search.models import CaServiceSearch
from useraccounts.models import User
import jsonfield


# Create your models here.

class CaService(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500, null=True, blank=True)
    features = jsonfield.JSONField()

    def __str__(self):
        return self.title


class CaServicesPrice(models.Model):
    service = models.ForeignKey(CaService, on_delete=models.CASCADE)
    ca = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(max_length=120)

    class Meta:
        unique_together = ["service", "ca"]
        index_together = ["service", "ca"]

    def __str__(self):
        return str(self.service.title) + " -- " + str(self.ca.full_name)

    def save(self, *args, **kwargs):
        super(CaServicesPrice, self).save(*args, **kwargs)

        CaServiceSearch.objects.update_or_create(
            search_string=self.service.name,
            ca=self.ca
        )


class ServiceInterest(models.Model):
    service = models.ForeignKey(CaService, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["service", "user"]
        index_together = ["service", "user"]


from services.models import Services

class CaServicePriceV2(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    ca = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return str(self.service.title) + " -- " + str(self.ca.full_name) + " -- " + str(self.price)
