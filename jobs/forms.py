from django import forms

from django import forms

from jobs.models import Company, Vacancy


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = (
            'name',
            'location',
            'logo',
            'description',
            'employee_count',
        )

        labels = {
            'name': "Название",
            'location': "Локация",
            'logo': "Логотип",
            'description': "Описание",
            'employee_count': "Количество сотрудников",
        }


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = (
            'title',
            'specialty',
            'description',
            'salary_min',
            'salary_max',
        )

        labels = {
            'title': "Название",
            'specialty': "Специальность",
            'description': "Описание",
            'salary_min': "Зарплата от",
            'salary_max': "Зарплата до",
        }
