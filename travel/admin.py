from django.contrib import admin
from travel.models import Location, Traveler, Contact

# Register your models here.

admin.site.register(Location)
admin.site.register(Traveler)
admin.site.register(Contact)
