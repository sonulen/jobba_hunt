from django.shortcuts import render, HttpResponse
from django.views import View


class MainPageView(View):
    template_name = "main.html"

    def get(self, request):
        return HttpResponse(self.template_name)


class VacaniesPageView(View):
    template_name = "vacancies.html"

    def get(self, request):
        return HttpResponse(self.template_name)


class SpecializationPageView(View):
    template_name = "specialization.html"

    def get(self, request, specialization: str):
        return HttpResponse(self.template_name + " " + specialization)


class CompanyPageView(View):
    template_name = "company.html"

    def get(self, request, id: int):
        return HttpResponse(self.template_name)


class JobPageView(View):
    template_name = "job.html"

    def get(self, request, id: int):
        return HttpResponse(self.template_name)


def custom_404(request, exception):
    return render(request, '404.html')
