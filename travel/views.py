from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Location, Traveler, Contact


# Create your views here.


class AboutView(View):
    template_name = ""

    def get(self, request):

        dest = Location.objects.all()
        traveler = Traveler.objects.all()
        return render(request, self.template_name, {"dest": dest, "traveler": traveler})

    def post(self, request):
        contact = Contact()
        contact.customername = request.POST.get("name")
        contact.email = request.POST.get("email")
        contact.subject = request.POST.get("subject")
        contact.message = request.POST.get("message")
        contact.save()

        return HttpResponse("thank you for your interaction")
