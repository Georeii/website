from django.shortcuts import render
from django.http import HttpResponseRedirect,request
from .models import People

# # Create your views here.

def entrance(response):
	return render(response,"main/entrance.html")

	


def registration(request):
	return render(request, "main/registration.html")


def create(request):
	if request.method == "POST":
	    people = People()
	    people.name = request.POST.get("name")
	    people.Email = request.POST.get("email")
	    people.password = request.POST.get("password")
	    people.surname = request.POST.get("surname")
	    people.phone_number = request.POST.get("phone_number")
	    people.save()
	return HttpResponseRedirect("/personal_area")

def personal_area(request):
	try:
		email = people.Email
		password= people.password
		name= people.name
		surname=people.surname
		data = {'email' : email, 'password':password, 'name':name, 'surname':surname}
		return render(request, "main/personal_area.html",data )
	except:
		return render(request, "main/personal_area.html" )

def companies(request):
	return render(request, "main/companies.html" )



def Peoples(request):
	return render(request, "main/Peoples.html" )



