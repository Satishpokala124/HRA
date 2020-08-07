from django import forms
from django.forms import ModelForm
from home.models import myUser,Property
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
	class Meta:
		model = myUser
		fields = ['username','first_name','last_name','email']
		widgets = {
		'username': forms.TextInput(attrs={"class":"myform-control","placeholder":"Enter Username"}),
		'first_name': forms.TextInput(attrs={"class":"myform-control","placeholder":"Enter first name"}),
		'last_name': forms.TextInput(attrs={"class":"myform-control","placeholder":"Enter last name"}),
		'email': forms.EmailInput(attrs={"class":"myform-control","placeholder":"Enter email"}),
		}

class AddPropertyForm(ModelForm):
	class Meta:
		model = Property
		fields = ['name','city','contact','address','image']
		widgets = {
		'name': forms.TextInput(attrs={"class":"myform-control","placeholder":"Enter Property name"}),
		'city': forms.Select(attrs={"class":"myform-control invert"}),
		'contact': forms.TextInput(attrs={"class":"myform-control"}),
		'address': forms.TextInput(attrs={"class":"myform-control"})
		}
		
