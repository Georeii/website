from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('registration',views.SignUp.as_view(), name = 'registration'),
    path('companies',views.companies, name = 'Companies'),
    path('People',views.Peoples, name = 'People'),
    path('personal_area',views.personal_area, name = 'Personal_area'),
=======
    path('personal_area',views.personal_area, name = 'personal_area'),
    path('registration',views.registration, name = 'registration'),
    path('entrance', views.entrance, name = 'entrance'),
    path('companies',views.companies, name = 'companies'),
    path('People',views.people, name = 'people'),
    path('create/',views.create,),
    path('entrance_pr', views.entrance_pr)
>>>>>>> 948e595a3b4c89cff48d883a75f8df1c3029a44f

]
