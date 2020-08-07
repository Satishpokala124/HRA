from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('index/', views.index, name='index'),
	path('signUp/<int:t>', views.signUp, name='signUp'),
	path('signIn/', auth_views.LoginView.as_view(template_name='home/signIn.html'), name='signIn'),
	path('home/', views.home, name='home'),
	path('signOut/', auth_views.LogoutView.as_view(template_name='home/home.html'), name='signOut'),
	path('properties/', views.properties, name='properties'),
	path('addProperty/', views.addProperty, name='addProperty'),
	path('propPage/<int:id>', views.propPage, name='propPage'),
	path('updateProperty/<int:id>', views.updateProperty, name='updateProperty'),
	path('deleteProperty/<int:id>', views.deleteProperty, name='deleteProperty'),
]