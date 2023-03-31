from django.shortcuts import render
from django.http import HttpResponseRedirect,request
from .models import People


def entrance(response):
	return render(response,"main/entrance.html")

	
def entrance_pr(request):
	pass


def registration(request):
	return render(request, "main/registration.html")


def create(request):
	email_pr = People.objects.get(email).count()
	if email_pr != 0:
		return HttpResponseRedirect("/registration")
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

def create_company(request):
	company = Company(name_company = request.POST.get("name_company"), people = people)
	company.save()



def Peoples(request):
	return render(request, "main/Peoples.html" )
