from django import forms
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class contactform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=contact

class signupform(UserCreationForm):
    class meta:
        fields=('first_name','last_name','username','email','password1','password2')
        model=User

class sellform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=properties