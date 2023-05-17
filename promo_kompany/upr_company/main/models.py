from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
	users = models.ManyToManyField(User)
	name_company = models.CharField(max_length=50)



class Home(models.Model):
	company = models.ManyToManyField("Company")
	city = models.TextField()
	street = models.TextField()
	num_home = models.CharField(max_length=10)
	col_apartment = models.FloatField()


class Bypass_result(models.Model):
	home = models.ForeignKey(Home, on_delete=models.CASCADE )
	apartment = models.FloatField()
	open_close = models.FloatField()
	reaction = models.FloatField()
	# open_close 1 открыто 0 закрыто
	# reaction 0 негативно, 1 нейтрально, 2 положительно 