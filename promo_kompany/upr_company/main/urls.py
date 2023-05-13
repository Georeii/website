from django.urls import path
from . import views

urlpatterns = [
    path('registration',views.SignUp.as_view(), name = 'registration'),
    path('companies',views.companies, name = 'Companies'),
    path('People',views.Peoples, name = 'People'),
    path('personal_area',views.personal_area, name = 'Personal_area'),

]
