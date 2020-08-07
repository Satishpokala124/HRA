from django.db import models
from django.contrib.auth.models import User
from .data import cityOptions

# Create your models here.

class myUser(User):
	is_Tenant = models.IntegerField(null=True)
	is_Landlord = models.IntegerField(null=True)
	def __str__(self):
		return self.username

class Property(models.Model):
	name = models.CharField(max_length=300)
	state = models.CharField(max_length=50)
	city = models.CharField(max_length=100, choices=cityOptions)
	address = models.CharField(max_length=500)
	contact = models.ChaField(max_length=10)
	is_Vacant = models.IntegerField()
	landLord = models.ForeignKey(myUser, on_delete=models.CASCADE)
	image = models.ImageField(upload_to = "Property/",null="True")