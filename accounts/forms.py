from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from accounts.models import CustomUser, Application


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('full_name', 'phone_number', 'written_cover_letter')
