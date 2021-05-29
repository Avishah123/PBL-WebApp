from django.contrib import admin
from . import views
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('enduser', views.enduser.as_view(), name='enduser'),
    path('manu', views.manufacturer.as_view(), name='manu'),
    path('provider', views.provider.as_view(), name='provider'),
    path('home', views.home, name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('login', auth_views.LoginView.as_view(
        template_name='forms/login.html'), name='login'),
    path('logout', views.logout, name='logout'),
    path('',views.index,name='index'),
    path('test',views.test1,name='test'),


] 
