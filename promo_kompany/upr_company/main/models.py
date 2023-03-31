from django.db import models


class People(models.Model):
	Email = models.CharField(max_length=50)
	password = models.CharField(max_length=32)
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=12)


class Company(models.Model):
	people = models.ManyToManyField(People)
	name_company = models.CharField(max_length=50)


class Home(models.Model):
	company = models.ManyToManyField(Company)
	city = models.TextField()
	street = models.TextField()
	num_home = models.CharField(max_length=10)
	entrase = models.FloatField()


class Bypass_result(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE )
	home = models.ForeignKey(Home, on_delete=models.CASCADE )
	apartment = models.FloatField()
	open_close = models.FloatField()
	reaction = models.FloatField()
	# open_close 1 открыто 0 закрыто
	# reaction 0 негативно, 1 нейтрально, 2 посыл в баню  