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


def create_company(request,id):
	company = Company()
	company.name_company = request.POST.get("name_company")
	company.save()
	company.users.add(id)
	return HttpResponseRedirect("/companies")


def change_company(request, id):
	company = Company.get(id)
	company.users.add(request.POST.get("people_id"))
# ---------------------------------------------------


def create_home(request,id):
	homes = Home.objects.filter(company =id)
	return render(request, "main/create_home.html", {"id" : id,"homes":homes})


def app_home(request,idr):
	if request.method == "POST":
		homes = Home()
		homes.city = request.POST.get("city")
		homes.street= request.POST.get("street")
		homes.num_home = request.POST.get("num_home")
		homes.col_apartment = request.POST.get("col_apartment")
		homes.save() 
		homes.company.add(idr)
	return HttpResponseRedirect(f"/create_home/{idr}/")


# -----------------------------------------------------
def fill_countdown(request,id):
	hm = Home.objects.filter(company = id)
	dr = []
	for i in hm:
		dr += Bypass_result.objects.filter(home = i)
		
	return render(request, "main/fill_countdown.html", {'Bypass_results':dr,"Homes":hm,"id" : id})
	# except:
	# return render(request, "main/fill_countdown.html", {"Homes":hm,"id" : id})



def fill_countdown_create(request,id):
	if request.method == "POST":
		br = Bypass_result()
		br.home_id = request.POST.get('home_id')
		br.apartment = request.POST.get("apartment")
		br.open_close = request.POST.get("un_open")
		br.reaction = request.POST.get("reaction")
		br.save()
	return HttpResponseRedirect(f"/fill_countdown/{id}/")
