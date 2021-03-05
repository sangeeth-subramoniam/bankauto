from django import forms
from django.contrib.auth.models import User
from .models import updimages

class updimages_form(forms.ModelForm):

    class Meta:
        model = updimages
        fields = ['user_profile','img','approval']
