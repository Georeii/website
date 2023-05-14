from django.shortcuts import render,redirect
from django.http import request,HttpResponseNotFound,HttpResponseRedirect
<<<<<<< HEAD

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Company


=======
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Company


# -------------------------------------------
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"
>>>>>>> main

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"

<<<<<<< HEAD

=======
>>>>>>> main
def personal_area(request):
	return render(request, "main/personal_area.html")


<<<<<<< HEAD
=======
def Peoples(request):
	users = User.objects.all()
	return render(request, "main/Peoples.html", {"users": users})
# --------------------------------------------

>>>>>>> main

def companies(request):
	company = Company.objects.all()
	return render(request, "main/companies.html", {"company":company} )


def create_company(request):
	company = Company(name_company = request.POST.get("name_company"), people = people)
	company.save()
	return HttpResponseRedirect("/companies")
# ---------------------------------------------------


def create_home(request):
	return render(request, "main/app_home.html")


def home():
	return render(request, "main/app_home.html")


def fill_countdown():
	return render(request, "main/.html")


def fill_countdown_create():
	pass