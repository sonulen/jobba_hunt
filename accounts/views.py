from django.http import Http404
from django.shortcuts import render, HttpResponse
from django.views import View


class JobResponseView(View):
    template_name = "job_response.html"

    def get(self, request):
        return HttpResponse(self.template_name)


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
