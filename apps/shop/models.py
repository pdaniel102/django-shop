from django.db import models
from numpy import blackman

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null= True, blank = True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url