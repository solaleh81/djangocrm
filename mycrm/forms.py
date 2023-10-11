from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

#Sign up
class SignUpForm(UserCreationForm):
    name = forms.CharField(lable="name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(lable="email", widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(lable="username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(lable="password", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(lable="password confirm", widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('name', 'email', 'username', 'password1', 'password2')