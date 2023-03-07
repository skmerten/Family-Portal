
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
#from django.utils.translation import ugettext_lazy as _
from datetime import datetime, timedelta


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
"""
class NewUserForm(forms.ModelForm):
    username = forms.CharField(label='User Name*', max_length=100, required=True, widget=forms.TextInput(attrs={'class' : 'input'}))
    password = forms.CharField(label='Password*', max_length=100, required=True, widget=forms.PasswordInput(attrs={'class' : 'input'}))
    email = forms.EmailField(label='Email Address*', max_length=100, required=True, widget=forms.EmailInput(attrs={'class' : 'input'}))
    first_name = forms.CharField(label='First Name', max_length=100, required=True, widget=forms.TextInput(attrs={'class' : 'input'}))
    last_name = forms.CharField(label='Last Name', max_length=100, required=True, widget=forms.TextInput(attrs={'class' : 'input'}))
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', )
"""