from django.db.models import Q
from django.db.models import QuerySet
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View

from accounts.forms import ApplicationForm
from jobs.models import (
    Specialty, Company, Vacancy
)


class MainView(View):
    template_name = "jobs/main.html"

    def get(self, request):
        example_keywords_for_search = [
            "Python",
            "Flask",
            "Django",
            "Парсинг",
            "ML",
        ]

        return render(
            request,
            self.template_name,
            context={
                "example_keywords": example_keywords_for_search,
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

        if request.user.is_authenticated:
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


class VacanciesSearchView(View):
    template_name = "jobs/search.html"

    def find_all_vacancies(self, keyword: str) -> QuerySet:
        return Vacancy.objects.filter(
            Q(title__contains=keyword) |
            Q(company__name__contains=keyword) |
            Q(specialty__title__contains=keyword) |
            Q(skills__title__contains=keyword)
        ).all()

    def get(self, request, keyword: str):
        vacancies = self.find_all_vacancies(keyword)

        return render(
            request,
            self.template_name,
            context={
                "keyword": keyword,
                "vacancies": vacancies
            }
        )

    def post(self, request, *args, **kwargs):
        keyword = request.POST.get("keyword", "")

        print(request.POST)
        print(keyword)

        if keyword:
            return redirect('search_vacancies', keyword=keyword)

        return redirect('main')


class AboutView(View):
    template_name = "jobs/about.html"

    def get(self, request):
        return render(
            request,
            self.template_name,
        )


def custom_404(request, exception):
    return render(request, '404.html')
