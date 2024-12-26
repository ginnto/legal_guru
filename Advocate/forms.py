from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AdvocateRegistration

class AdvocateRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    specialization = forms.CharField(max_length=100)
    officename = forms.CharField(max_length=30)
    place = forms.CharField(max_length=30)
    state = forms.CharField(max_length=20)
    district = forms.CharField(max_length=20)
    postoffice = forms.CharField(max_length=20)
    pincode = forms.CharField(max_length=10)
    contactno = forms.CharField(max_length=10)
    image = forms.ImageField()
    aadharno = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        advocate = AdvocateRegistration(
            user=user,
            specialization=self.cleaned_data['specialization'],
            officename=self.cleaned_data['officename'],
            place=self.cleaned_data['place'],
            state=self.cleaned_data['state'],
            district=self.cleaned_data['district'],
            postoffice=self.cleaned_data['postoffice'],
            pincode=self.cleaned_data['pincode'],
            contactno=self.cleaned_data['contactno'],
            image=self.cleaned_data['image'],
            aadharno=self.cleaned_data['aadharno']
        )
        advocate.save()
        return user
