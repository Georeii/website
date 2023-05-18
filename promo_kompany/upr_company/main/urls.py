from django.urls import path
from . import views

urlpatterns = [
    # люди
    path('personal_area',views.personal_area, name = 'Personal_area'),
    path('People',views.Peoples, name = 'People'),
    path('registration',views.SignUp.as_view(), name = 'registration'),
    # -----------------------------
    # компании
    path('companies',views.companies, name = 'Companies'),
    path('create_company/<int:id>/',views.create_company, name = 'Сreate_company'),
    path('change_company/<int:id>/',views.change_company, name = 'Change_company'),
   # -------------------------------
    path("create_home/<int:id>/",views.create_home, name ="create_home"),
    path("app_home/<int:idr>/",views.app_home, name = "app_home"),
    path("fill_countdown/<int:id>/",views.fill_countdown, name = "fill_countdown"),
    path("fill_countdown_create/<int:id>/",views.fill_countdown_create, name = "fill_countdown_create"),



]
