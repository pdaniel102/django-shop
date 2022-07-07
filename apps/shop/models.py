from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    digital = models.BooleanField(default=False, null=True, blank=True)
    #image

    def __str__(self):
        return self.name