from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name","last_name")

        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields=("rut","tipo_usuario")


