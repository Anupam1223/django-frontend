from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Location


# Create your views here.


class AboutView(View):
    template_name = "index.html"

    def get(self, request):

        dest = Location.objects.all()
        return render(request, "index.html", {"dest": dest})
