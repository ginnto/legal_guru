from django.db import models
from Advocate.models import *

# Create your models here.

class CaseRequest(models.Model):
    req_id = models.AutoField(primary_key=True)
    lawyer = models.ForeignKey(AdvocateRegistration,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=11)
    case_des = models.TextField()
    approval = models.CharField(max_length=50, choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending')
    cust_approval = models.CharField(max_length=50, choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"CaseRequest #{self.req_id} - {self.name}"


