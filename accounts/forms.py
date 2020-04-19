from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from accounts.models import CustomUser, Application, Resume


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
        labels = {
            'email': "Почта",
            'first_name': "Имя",
            'last_name': "Фамилия",
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
        labels = {
            'email': "Почта",
            'first_name': "Имя",
            'last_name': "Фамилия",
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('full_name', 'phone_number', 'written_cover_letter')
        labels = {
            'full_name': "Полное имя",
            'phone_number': "Телефон",
            'written_cover_letter': "Сопроводительно письмо",
        }


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = (
            'status',
            'salary',
            'specialty',
            'grade',
            'education',
            'experience',
            'portfolio',
        )

        labels = {
            'status': "Статус",
            'salary': "Зарплата",
            'specialty': "Специальность",
            'grade': "Грейд",
            'education': "Образование",
            'experience': "Опыт",
            'portfolio': "Портфолио",
        }
