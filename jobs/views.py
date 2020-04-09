from django.http import Http404
from django.shortcuts import render
from django.views import View

from jobs.models import (
    Specialty, Company, Vacancy
)


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


class SpecializationView(View):
    template_name = "jobs/specialization.html"

    def get(self, request, specialization: str):
        specialization = Specialty.objects.filter(code=specialization).first()

        if specialization == None:
            raise Http404

        return render(
            request,
            self.template_name,
            context={
                "specialization": specialization,
                "vacancies": Vacancy.objects.filter(specialty__code=specialization).all().order_by('-published_at')
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


class JobView(View):
    template_name = "jobs/job.html"

    def get(self, request, id: int):
        vacancy = Vacancy.objects.filter(pk=id).first()
        if vacancy == None:
            raise Http404

        return render(
            request,
            self.template_name,
            context={
                "vacancy": Vacancy.objects.filter(pk=id).first()
            }
        )


def custom_404(request, exception):
    return render(request, '404.html')
