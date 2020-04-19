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
