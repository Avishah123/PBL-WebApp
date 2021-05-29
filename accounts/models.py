from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    state = models.CharField(max_length=254)
    email =models.CharField(max_length=254)
    is_enduser = models.BooleanField(default=False)
    is_manufacturer = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    mail_sent = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)


class EndUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    date_of_birth = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    pincode = models.CharField(max_length=254)
    state = models.CharField(max_length=254)
    doses = models.CharField(max_length=254)
    id_proof = models.ImageField(upload_to='images/Id Proof/enduser')
    aadhar = models.CharField(max_length=254)
    is_verified = models.BooleanField(default=False)
    mail_sent = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class manufacturer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    date_of_birth = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    pincode = models.CharField(max_length=254)
    state = models.CharField(max_length=254)
    id_proof = models.ImageField(upload_to='images/Id Proof/manufacturer')
    gst = models.CharField(max_length=254)
    doses = models.CharField(max_length=254)
    position = models.CharField(max_length=254)
    is_verified = models.BooleanField(default=False)
    mail_sent = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class provider(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    mobile_number = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    date_of_birth = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    pincode = models.CharField(max_length=254)
    state = models.CharField(max_length=254)
    id_proof = models.ImageField(upload_to='images/Id Proof/manufacturer')
    gst = models.CharField(max_length=254)
    position = models.CharField(max_length=254)
    doses = models.CharField(max_length=254)
    is_verified = models.BooleanField(default=False)
    mail_sent = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
