from django.shortcuts import render
from django.views import View
from jobs.models import (
    Specialty, Company
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
            }
        )


class SpecializationPageView(View):
    template_name = "jobs/specialization.html"

    def get(self, request, specialization: str):
        return render(
            request,
            self.template_name,
            context={
            }
        )


class CompanyPageView(View):
    template_name = "jobs/company.html"

    def get(self, request, id: int):
        return render(
            request,
            self.template_name,
            context={
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
