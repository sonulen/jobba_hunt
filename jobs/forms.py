from django import forms

from django import forms

from jobs.models import Company
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML


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
