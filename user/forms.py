from .models import UserProfileInfo
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    ''' Form for create a username, password and email fields for User '''

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    ''' Form for create a portfolio_img fields for User '''

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_img',)
