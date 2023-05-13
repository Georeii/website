from django.shortcuts import render,redirect
from django.http import request,HttpResponseNotFound,HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Company



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"


def personal_area(request):
	return render(request, "main/personal_area.html")



def companies(request):
	return render(request, "main/companies.html" )

def create_company(request):
	company = Company(name_company = request.POST.get("name_company"), people = people)
	company.save()
	return HttpResponseRedirect("/companies")



def Peoples(request):
	return render(request, "main/Peoples.html" )
