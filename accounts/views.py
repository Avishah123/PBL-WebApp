from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import CreateView
from django.contrib.auth import login
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
import csv
from django.http import HttpResponse
from django.contrib import auth
from .models import *
from django.template.loader import render_to_string
import requests

# Create your views here.

# def enduser(request):
#     return render(request, 'forms/enduserSignup.html')
class enduser(CreateView):
    model = User
    form_class = EnduserSignUpForm
    template_name = 'forms/enduserSignup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        email=form.cleaned_data.get('email')
        subject = 'You have been registered for Vaccine'
        from_email = settings.DEFAULT_FROM_EMAIL
        message = 'Test'
        html_message = 'You are registered for the vaccine , you will get notified once you get verified'

        send_mail(subject, message, from_email,[email,'getavi4@gmail.com'],
                      fail_silently=False, html_message=html_message)

        return redirect('dashboard')


class manufacturer(CreateView):
    model = User
    form_class = ManufacturerSignUpForm
    template_name = 'forms/manuSignup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        email=form.cleaned_data.get('email')
        subject = 'You have been registered for Vaccine'
        from_email = settings.DEFAULT_FROM_EMAIL
        message = 'Test'
        html_message = 'You are registered for the vaccine , you will get notified once you get verified'

        send_mail(subject, message, from_email,[email,'getavi4@gmail.com'],
                      fail_silently=False, html_message=html_message)

        return redirect('dashboard')


class provider(CreateView):
    model = User
    form_class = ProviderSignUpForm
    template_name = 'forms/providerSignup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        email=form.cleaned_data.get('email')
        subject = 'Techela 6.0 Registration'
        from_email = settings.DEFAULT_FROM_EMAIL
        message = 'Test'
        html_message = 'You are registered'

        send_mail(subject, message, from_email,[email,'getavi4@gmail.com'],
                      fail_silently=False, html_message=html_message)

        return redirect('dashboard')


def home(request):
    return render(request, 'home.html')

# request.user.username

@login_required
def dashboard(request):


    state =  request.user.state 
    state  = state.lower()

    api_address = "https://api.covid19india.org/data.json"
    json_data = requests.get(api_address).json()
    state_indexing = range(0,30)

    for n in state_indexing:
        if state == json_data['statewise'][n]['state'].lower():
            Confirmed_Case = json_data['statewise'][n]['confirmed']
        n+= 1

    for n in state_indexing:
        if state == json_data['statewise'][n]['state'].lower():
            recovered_Case = json_data['statewise'][n]['recovered']
        n+= 1

    for n in state_indexing:
        if state == json_data['statewise'][n]['state'].lower():
            deaths_Case = json_data['statewise'][n]['deaths']
        n+= 1

    context = {
        'cases1' : Confirmed_Case,
        'cases2' : recovered_Case,
        'cases3' : deaths_Case,
    }
    
    print(f"Active Case in {state} is {Confirmed_Case}")
    print(f"Recovered Cases in {state} is {recovered_Case}")
    print(f"Deaths Case in {state} is {deaths_Case}")

    return render(request, 'dashboard.html',context)  


@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')

def registration_page(request):
    return render(request , 'registration.html')

def index(request):
    return render(request,'index.html')

def test1(request):
    citizen = User.objects.all()

    context = {
        'citizen' : citizen,
    }

    return render(request,'test.html')