from django.db import models

# Create your models here.

class Vehicles(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name
