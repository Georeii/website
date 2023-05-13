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
<<<<<<< HEAD
	return render(request, "main/personal_area.html")

=======
	people = People()
	Email = people.Email
	password= people.password
	name= people.name
	surname=people.surname
	data = {'Email' : Email, 'password':password, 'name':name, 'surname':surname}
	return render(request, "main/personal_area.html",data )
>>>>>>> 948e595a3b4c89cff48d883a75f8df1c3029a44f


def companies(request):
	return render(request, "main/companies.html" )

def create_company(request):
	company = Company(name_company = request.POST.get("name_company"), people = people)
	company.save()
	return HttpResponseRedirect("/companies")



def peoples(request):
	person = People()
	person = People.objects.all()
	return render(request, "main/Peoples.html" )
