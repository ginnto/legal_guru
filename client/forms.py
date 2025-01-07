from django import forms
from .models import Feedback
from home.models import Payment

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback', 'rating']
        widgets = {
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }




class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['case', 'account_number', 'cvv', 'expiry_date', 'amount_paid']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }
