from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD

    path('registration',views.SignUp.as_view(), name = 'registration'),
    path('companies',views.companies, name = 'Companies'),
    path('People',views.Peoples, name = 'People'),
    path('personal_area',views.personal_area, name = 'Personal_area'),


=======
    # люди
    path('personal_area',views.personal_area, name = 'Personal_area'),
    path('People',views.Peoples, name = 'People'),
    path('registration',views.SignUp.as_view(), name = 'registration'),
    # -----------------------------
    # компании
    path('companies',views.companies, name = 'Companies'),
    path('create_company',views.create_company, name = 'Сreate_company'),
   # -------------------------------
    path("create_home",views.create_company, name = "create_company"),
    path("home",views.home, name ="home"),
    path("create_home",views.create_home, name = "create_home"),

>>>>>>> main
]
