from django.urls import path
from . import views

urlpatterns = [
    path('personal_area',views.personal_area, name = 'personal_area'),
    path('registration',views.registration, name = 'registration'),
    path('entrance', views.entrance, name = 'entrance'),
    path('companies',views.companies, name = 'companies'),
    path('People',views.people, name = 'people'),
    path('create/',views.create,),
    path('entrance_pr', views.entrance_pr)

]
