from django.shortcuts import render
from django.http import HttpResponseRedirect,request,HttpResponseNotFound
from .models import People, Company

# вход
def entrance(response): #страница входа
	return render(response,"main/entrance.html")


def entrance_pr(request):# проверка входа
	verified = People()
	verified = People.objects.all()
	verifiable_email = request.POST.get("Email")
	verifiable_password = request.POST.get("password")
	try:
		for i in verified: 
			if i.Email ==  verifiable_email:
				if  i.password == verifiable_password:
					people = {'Email' : Email, 'password':password, 'name':name, 'surname':surname}
					return HttpResponseRedirect("/personal_area"), people
	except:
		return HttpResponseNotFound("<h2>Person not found</h2>")

# регистрация
def registration(request):# страница регистрации
	return render(request, "main/registration.html")


def create(request):# добавления в бд
	email_pr = People.objects.get(Email).count()
	if email_pr != 0:
		return HttpResponseRedirect("/registration")
	elif request.method == "POST":
	    people = People()
	    people.name = request.POST.get("name")
	    people.Email = request.POST.get("Email")
	    people.password = request.POST.get("password")
	    people.surname = request.POST.get("surname")
	    people.phone_number = request.POST.get("phone_number")
	    people.save()
	return HttpResponseRedirect("/personal_area")
# 
# личные кабинеты ----------
def personal_area_rt(request, data):# зарегистрированый пользователь

	data = {'email' : email, 'password':password, 'name':name, 'surname':surname}
	return render(request, "main/personal_area.html",data )


def personal_area(request):# гость
	return render(request, "main/personal_area.html" )
# ------------------------------

# 
def companies(request):
	return render(request, "main/companies.html" )

def create_company(request):
	company = Company(name_company = request.POST.get("name_company"), people = people)
	company.save()
	return HttpResponseRedirect("/companies")
# 

# 
def Peoples(request):
	return render(request, "main/Peoples.html" )
# 
