from django.shortcuts import render
from django.http import Http404
from django.views import View
from jobs.models import (
    Specialty, Company, Vacancy
)


class MainPageView(View):
    template_name = "jobs/main.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={
                "specialties": Specialty.objects.all()[:8],
                "companies": Company.objects.all()
            }
        )


class VacanciesPageView(View):
    template_name = "jobs/vacancies.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
            context={
                "vacancies": Vacancy.objects.all().order_by('-published_at')
            }
        )


class SpecializationPageView(View):
    template_name = "jobs/specialization.html"

    def get(self, request, specialization: str):
        if Specialty.objects.filter(code=specialization).first() == None:
            raise Http404

        return render(
            request,
            self.template_name,
            context={
                "specialization": Specialty.objects.filter(code=specialization).first(),
                "vacancies": Vacancy.objects.filter(specialty__code=specialization).all().order_by('-published_at')
            }
        )


class CompanyPageView(View):
    template_name = "jobs/company.html"

    def get(self, request, id: int):
        if Company.objects.filter(pk=id).first() == None:
            raise Http404

        return render(
            request,
            self.template_name,
            context={
                "company": Company.objects.filter(pk=id).first(),
                "vacancies": Vacancy.objects.filter(company__pk=id).all().order_by('-published_at')
            }
        )


class JobPageView(View):
    template_name = "jobs/job.html"

    def get(self, request, id: int):
        return render(
            request,
            self.template_name,
            context={
            }
        )


def custom_404(request, exception):
    return render(request, '404.html')
