from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,AddPropertyForm
from .models import myUser,Property
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .data import city_idToStateName,cityDict,cityOptions
from django.views.decorators.cache import cache_control

# Create your views here.

def index(request):
	return render(request, 'home/index.html')

def signUp(request, t):
	if request.method == "POST":
		user = SignUpForm(request.POST)
		username = request.POST['username']
		email = request.POST['email']
		if len(list(User.objects.all().filter(username=username))):
			messages.warning(request, "Username has been taken")
		elif len(list(User.objects.all().filter(email = email))):
			messages.warning(request, "Email already exists")
		elif user.is_valid():
			obj = user.save(commit=False)
			obj.is_Tenant = int(t)
			obj.is_Landlord = int(not t)
			obj.save()
			return redirect('home')
		else:
			messages.warning(request, "Please enter valid details")
	form = SignUpForm()
	return render(request, 'home/signUp.html', {'form': form, 't':t})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
	cities = [i.city for i in Property.objects.all()]
	cities = list(set(cities))
	id = request.user.id
	user = myUser.objects.all().get(id=id)
	is_Tenant = user.is_Tenant
	if is_Tenant:
		if request.method =="POST":
			city = request.POST['city']
			props = Property.objects.all().filter(city=city,is_Vacant=1)
			return render(request, 'home/tHome.html', {'user': user, 'props': props, 'cities':cities})
		return render(request, 'home/tHome.html', {'user': user, 'props':False, 'cities':cities})
	else :
		return render(request, 'home/lHome.html', {'user': user})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def properties(request):
	props = Property.objects.filter(landLord_id = request.user.id)
	if not len(list(props)):
		print(list(props))
		return render(request, 'home/properties.html', {'props': False})
	return render(request, 'home/properties.html', {'props': props})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addProperty(request):
	form = AddPropertyForm()
	if request.method == "POST":
		name = request.POST['name']
		prop = AddPropertyForm(request.POST,request.FILES)
		city = request.POST['city']
		if len(list(Property.objects.filter(name=name))):
			messages.warning(request, "A property already exists with this name"+name)
			return render(request, 'home/addProperty.html', {'form':form})
		propObj = prop.save(commit=False)
		propObj.state = city_idToStateName[city]
		propObj.city = cityDict[city]
		propObj.landLord_id = request.user.id
		propObj.is_Vacant = 1
		propObj.save()
		return redirect('properties')
	form = AddPropertyForm()
	return render(request, 'home/addProperty.html', {'form':form})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def propPage(request, id):
	property = Property.objects.get(id=id)
	landlord = myUser.objects.get(id=property.landLord_id)
	user =  myUser.objects.get(id=request.user.id)
	return render(request, 'home/propPage.html', {'property':property, 'landlord':landlord, 'user': user})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateProperty(request, id):
	instance = Property.objects.get(id=id)
	if request.method == "POST":
		city = request.POST['city']
		name = request.POST['name']
		prop = AddPropertyForm(request.POST, request.FILES, instance=instance)
		vacancy = request.POST['vacancy']
		if len(list(Property.objects.filter(name=name))) and name != instance.name:
			messages.warning(request, "A property already exists with this name "+name)
			return render(request, 'home/updateProperty.html', {'prop':prop})
		if prop.is_valid():
			propObj = prop.save(commit=False)
			propObj.state = city_idToStateName[city]
			propObj.city = cityDict[city]
			propObj.landLord_id = request.user.id
			propObj.is_Vacant = int(vacancy)
			propObj.save()
			return redirect('properties')
	prop = AddPropertyForm(instance=instance)
	return render(request, 'home/updateProperty.html', {'prop': prop})

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deleteProperty(request, id):
	prop = Property.objects.get(id=id)
	prop.delete()
	props = Property.objects.filter(landLord_id=request.user.id)
	return render(request, 'home/properties.html', {'props': props})