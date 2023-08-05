from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']
class ContactForm(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()
    content=forms.Textarea()