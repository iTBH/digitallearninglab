from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import DllUser


class EditUserForm(forms.ModelForm):
    class Meta:
        model = DllUser
        fields = ['email']


class SignUpForm(UserCreationForm):
    terms_accepted = forms.BooleanField()

    class Meta:
        model = DllUser
        fields = (
            'username',
            'gender',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'terms_accepted'
        )
