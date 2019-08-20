from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User


class PostForm(forms.Form):
    title = forms.CharField(max_length=250)
    content = forms.Textarea()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput)


# Adding new fields to UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# ModelForm allows us to work with specific database model
# User updation form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]  # fields that needs to be updated


# Profile updation form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]

