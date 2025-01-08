from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class specializations(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('/',args=[self.slug])

class AdvocateRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.ForeignKey(specializations,on_delete=models.CASCADE)
    officename = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    postoffice = models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)
    contactno = models.CharField(max_length=10)
    image = models.ImageField(upload_to='uploads/')
    aadharno = models.BigIntegerField()
    admin_approval = models.CharField(
        max_length=20,
        default='not approved',
        choices=[('approved', 'Approved'), ('not approved', 'Not Approved')]
    )

    def __str__(self):
        return self.user.username


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_Advocate_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_Advocate_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} at {self.created_at}"
