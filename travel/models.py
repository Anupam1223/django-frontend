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


class Traveler(models.Model):
    travelername = models.CharField(max_length=100)
    review = models.CharField(max_length=300)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/", default="")

    def __str__(self):
        return self.travelername


class Contact(models.Model):
    customername = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.customername
