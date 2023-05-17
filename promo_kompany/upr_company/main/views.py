from django.shortcuts import render,redirect
from django.http import request,HttpResponseNotFound,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import Company, Bypass_result,Home


# -------------------------------------------
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"


def personal_area(request):
	return render(request, "main/personal_area.html")


def Peoples(request):
	users = User.objects.all()
	return render(request, "main/Peoples.html", {"users": users})
# --------------------------------------------


def companies(request):
	company = Company.objects.all()
	return render(request, "main/companies.html", {"company":company} )


def create_company(request):
	company = Company(name_company = request.POST.get("name_company"), people = people)
	company.save()
	return HttpResponseRedirect("/companies")
# ---------------------------------------------------


def create_home(request,id):
	try:
		homes = Home.objects.get(company =id)
		return render(request, "main/create_home.html", {"id" : id,"homes":homes})
	except:
		return render(request, "main/create_home.html", {"id" : id})




def app_home(request,idr):
	if request.method == "POST":
		homes = Home()
		homes.city = request.POST.get("city")
		homes.street= request.POST.get("street")
		homes.num_home = request.POST.get("num_home")
		homes.col_apartment = request.POST.get("col_apartment")
		company = Company.objects.filter(id=idr)
		homes.company.set(company)  
	return HttpResponseRedirect(f"/create_home/{idr}/")


# -----------------------------------------------------
def fill_countdown(request,id):
	hm = Home.objects.filter(company = id)
	dr = Bypass_result.objects.all()
	# dr = []
	# try:
	# 	for i in dr_no:
	# 		if i in hm.id:
	# 			br.append(i)
	return render(request, "main/fill_countdown.html", {'Bypass_results':dr,"Homes":hm,"id" : id})
	# except:
	# return render(request, "main/fill_countdown.html", {"Homes":hm,"id" : id})



def fill_countdown_create(request,id):
	if request.method == "POST":
		h = Home()
		br = Bypass_result()
		# brid = 
		br.home_id = request.POST.get('home_id')
		br.apartment = request.POST.get("apartment")
		br.open_close = request.POST.get("un_open")
		br.reaction = request.POST.get("reaction")
		br.save()
	return HttpResponseRedirect(f"/fill_countdown/{id}/")
