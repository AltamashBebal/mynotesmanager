from django import forms

from .models import UsersNew

class UsersNewModel(forms.ModelForm):
    class Meta:
        model = UsersNew
        fields = ['image']

