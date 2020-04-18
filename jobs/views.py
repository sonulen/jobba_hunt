from django.http import Http404
from django.shortcuts import render
from django.views import View

from jobs.models import (
    Specialty, Company, Vacancy
)
from accounts.forms import ApplicationForm


class MainView(View):
    template_name = "jobs/main.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={
                "specialties": Specialty.objects.all(),
                "companies": Company.objects.all()
            }
        )


class VacanciesView(View):
    template_name = "jobs/vacancies.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={
                "vacancies": Vacancy.objects.all().order_by('-published_at')
            }
        )


class JobView(View):
    template_name = "jobs/job.html"

    def get(self, request, id: int):
        vacancy = Vacancy.objects.filter(pk=id).first()
        if vacancy == None:
            raise Http404

        if request.user is not None:
            form = ApplicationForm(initial={'full_name': request.user.get_full_name()})
        else:
            form = ApplicationForm()

        return render(
            request,
            self.template_name,
            context={
                "vacancy": vacancy,
                'form': form
            }
        )


class SpecializationView(View):
    template_name = "jobs/specialization.html"

    def get(self, request, specialization: str):
        selected_specialization = Specialty.objects.filter(code=specialization).first()

        if selected_specialization == None:
            raise Http404

        return render(
            request,
            self.template_name,
            context={
                "specialization": selected_specialization,
                "vacancies": Vacancy.objects.filter(specialty__code=specialization).all().order_by('-published_at')
            }
        )


class CompaniesView(View):
    template_name = "jobs/all_companies.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={
                "companies": Company.objects.all()
            }
        )


class CompanyView(View):
    template_name = "jobs/company.html"

    def get(self, request, id: int):
        company = Company.objects.filter(pk=id).first()
        if company == None:
            raise Http404

        return render(
            request,
            self.template_name,
            context={
                "company": company,
                "vacancies": Vacancy.objects.filter(company__pk=id).all().order_by('-published_at')
            }
        )


def custom_404(request, exception):
    return render(request, '404.html')
