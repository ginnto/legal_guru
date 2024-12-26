from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class AdvocateRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    officename = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    postoffice = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)
    contactno = models.CharField(max_length=10)
    image = models.ImageField(upload_to='uploads/')
    aadharno = models.BigIntegerField()

    def __str__(self):
        return self.user.username