from django.http import Http404
from django.shortcuts import render, HttpResponse
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
                "vacancy": vacancy
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


class JobResponseView(View):
    template_name = "job_response.html"

    def get(self, request):
        return HttpResponse(self.template_name)


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


class UserResumeView(View):
    template_name = "user_resume.html"

    def get(self, request):
        return HttpResponse(self.template_name)


class UserCompanyView(View):
    template_name = "user_company.html"

    def get(self, request):
        return HttpResponse(self.template_name)


class UserCompanyVacancies(View):
    template_name = "user_company_vacancies.html"

    def get(self, request):
        return HttpResponse(self.template_name)


class UserCompanyJob(View):
    template_name = "user_company_job.html"

    def get(self, request, id: int):
        return HttpResponse(self.template_name)


def custom_404(request, exception):
    return render(request, '404.html')
