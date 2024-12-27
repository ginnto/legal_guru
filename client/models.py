from django.db import models
from django.contrib.auth.models import User

class ClientRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Linking client to a User model
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    hname = models.CharField(max_length=40)
    place = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    district = models.CharField(max_length=20)
    postoffice = models.CharField(max_length=20)
    pin = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    contactno = models.CharField(max_length=12)
    image = models.ImageField(upload_to='client_images/', null=True, blank=True)  # Assuming images will be uploaded
    aadharno = models.BigIntegerField()  # Aadhar number as a large integer

    def __str__(self):
        return self.name

# Create your models here.
