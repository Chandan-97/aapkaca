from django.db import models


# Create your models here.

class CaService(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)


# class CaServicesPrice(models.Model):
#     service = models.ForeignKey(CaService, on_delete=models.CASCADE)
#     ca = models.ForeignKey(UserCa, on_delete=models.CASCADE)
#     price = models.IntegerField()
#     description = models.TextField(max_length=120)
#
#     class Meta:
#         unique_together = ["service", "ca"]
#         index_together = ["service", "ca"]
