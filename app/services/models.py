from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=255)
    starting_price = models.PositiveIntegerField()

    def __str__(self):
        return self.title
