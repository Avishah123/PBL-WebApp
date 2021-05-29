from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.exceptions import ValidationError


state_choices = [
    ('Andhra Pradesh','Andhra Pradesh'),('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),('Bihar','Bihar'),('Chhattisgarh','Chhattisgarh'),('Goa','Goa'),
    ('Gujarat','Gujarat'),('Haryana','Haryana'),('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),('Karnataka','Karnataka'),('Kerala','Kerala'),('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),('Manipur','Manipur'),('Meghalaya','Meghalaya'),('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),('Odisha','Odisha'),('Punjab','Punjab'),('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),('Tamil Nadu','Tamil Nadu'),('Telangana','Telangana'),('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),('Uttar Pradesh','Uttar Pradesh'),('West Bengal','West Bengal'),
]

class EnduserSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    mobile_number = forms.CharField(required=True)
    city = forms.CharField(required=True)
    email = forms.CharField(required=True)
    date_of_birth = forms.CharField(required=True)
    address = forms.CharField(required=True)
    pincode = forms.CharField(required=True)
    state = forms.CharField(required=True)
    id_proof = forms.ImageField(required=True)
    aadhar_number = forms.CharField(required=True)

    field_order = ['username','first_name','last_name','mobile_number','email','city','state','address','pincode','date_of_birth','id_proof','aadhar_number','password1','password2',]

    # Custom Validation for Aadhar card
    def clean_aadhar(self):
        aadhar = self.cleaned_data['aadhar_number']
        if len(aadhar) != 12 :
            raise forms.ValidationError("only 12 digits are accepted as input !")
        return aadhar

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise ValidationError((f"{email} is taken."),params = {'value':email})
        return email




    class Meta(UserCreationForm.Meta):
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder' : 'Username'}),
            
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_enduser = True
        user.state = self.cleaned_data.get('state')
        user.email = self.cleaned_data.get('email')

        user.save()
        enduser = EndUser.objects.create(user=user)
        enduser.email = self.cleaned_data.get('email')
        enduser.first_name = self.cleaned_data.get('first_name')
        enduser.last_name = self.cleaned_data.get('last_name')
        enduser.mobile_number = self.cleaned_data.get('mobile_number')
        enduser.city = self.cleaned_data.get('city')
        enduser.email = self.cleaned_data.get('email')
        enduser.date_of_birth = self.cleaned_data.get('date_of_birth')
        enduser.address = self.cleaned_data.get('address')
        enduser.pincode = self.cleaned_data.get('pincode')
        enduser.state = self.cleaned_data.get('state')
        enduser.id_proof = self.cleaned_data.get('id_proof')
        enduser.aadhar = self.cleaned_data.get('aadhar_number')
        enduser.save()

        return user


class ManufacturerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    mobile_number = forms.CharField(required=True)
    city = forms.CharField(required=True)
    email = forms.CharField(required=True)
    date_of_birth = forms.CharField(required=True)
    address = forms.CharField(required=True)
    pincode = forms.CharField(required=True)
    state = forms.CharField(required=True)
    id_proof = forms.ImageField(required=True)
    gst = forms.CharField(required=True)
    position = forms.CharField(required=True)
    doses = forms.IntegerField(required=True)

    field_order = ['username','first_name','last_name','mobile_number','email','city','state','address','pincode','date_of_birth','id_proof','gst','doses','position','password1','password2',]


    # Adding validation here that it has to be equal to 12 digits
    def clean_gst(self):
        gst = self.cleaned_data['gst']
        if len(gst) != 12 :
            raise forms.ValidationError("only 12 digits are accepted as input !")
        return gst

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise ValidationError((f"{email} is taken."),params = {'value':email})
        return email

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manufacturer = True
        user.email = self.cleaned_data.get('email')
        user.state = self.cleaned_data.get('state')

        user.save()
        enduser = manufacturer.objects.create(user=user)
        enduser.email = self.cleaned_data.get('email')
        enduser.first_name = self.cleaned_data.get('first_name')
        enduser.last_name = self.cleaned_data.get('last_name')
        enduser.mobile_number = self.cleaned_data.get('mobile_number')
        enduser.city = self.cleaned_data.get('city')
        enduser.email = self.cleaned_data.get('email')
        enduser.date_of_birth = self.cleaned_data.get('date_of_birth')
        enduser.address = self.cleaned_data.get('address')
        enduser.pincode = self.cleaned_data.get('pincode')
        enduser.state = self.cleaned_data.get('state')
        enduser.id_proof = self.cleaned_data.get('id_proof')
        enduser.gst = self.cleaned_data.get('gst')
        enduser.position = self.cleaned_data.get('position')
        enduser.doses = self.cleaned_data.get('doses')
        enduser.save()

        return user


# Provider Registration Form View

class ProviderSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    mobile_number = forms.CharField(required=True)
    city = forms.CharField(required=True)
    email = forms.CharField(required=True)
    date_of_birth = forms.CharField(required=True)
    address = forms.CharField(required=True)
    pincode = forms.CharField(required=True)
    state = forms.CharField(required=True)
    id_proof = forms.ImageField(required=True)
    gst = forms.CharField(required=True)
    position = forms.CharField(required=True)
    doses = forms.CharField(required=True)


    field_order = ['username','first_name','last_name','mobile_number','email','city','state','address','pincode','date_of_birth','id_proof','gst','doses','position','password1','password2',]

    def clean_gst(self):
        gst = self.cleaned_data['gst']
        if len(gst) != 12 :
            raise forms.ValidationError("only 12 digits are accepted as input !")
        return gst

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise ValidationError((f"{email} is taken."),params = {'value':email})
        return email
    
    
    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_provider = True
        user.email = self.cleaned_data.get('email')
        user.state = self.cleaned_data.get('state')

        user.save()
        enduser = provider.objects.create(user=user)
        enduser.email = self.cleaned_data.get('email')
        enduser.first_name = self.cleaned_data.get('first_name')
        enduser.last_name = self.cleaned_data.get('last_name')
        enduser.mobile_number = self.cleaned_data.get('mobile_number')
        enduser.city = self.cleaned_data.get('city')
        enduser.email = self.cleaned_data.get('email')
        enduser.date_of_birth = self.cleaned_data.get('date_of_birth')
        enduser.address = self.cleaned_data.get('address')
        enduser.pincode = self.cleaned_data.get('pincode')
        enduser.state = self.cleaned_data.get('state')
        enduser.id_proof = self.cleaned_data.get('id_proof')
        enduser.gst = self.cleaned_data.get('gst')
        enduser.position = self.cleaned_data.get('position')
        enduser.doses = self.cleaned_data.get('doses')

        enduser.save()

        return user
 