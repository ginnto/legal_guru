from django.contrib.auth.models import User
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
    payment_approval = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid')

    def __str__(self):
        return f"CaseRequest #{self.req_id} - {self.name}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who made the payment
    case = models.ForeignKey(CaseRequest, on_delete=models.CASCADE)  # Link to the case being paid for
    account_number = models.CharField(max_length=20)
    cvv = models.CharField(max_length=3)
    expiry_date = models.DateField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.case} by {self.user}"


