from django.urls import path
from . import views

urlpatterns = [
    path('personal_area',views.personal_area, name = 'Personal_area'),
    path('registration',views.registration, name = 'registration'),
    path('entrance', views.entrance, name = 'Entrance'),
    path('companies',views.companies, name = 'Companies'),
    path('People',views.People, name = 'People'),
    path('create/',views.create,),
    path('entrance_pr', views.entrance_pr)
    path('personal_area_rt',views.personal_area(people), name = 'Personal_area')

]
