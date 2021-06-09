from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
    package = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name
