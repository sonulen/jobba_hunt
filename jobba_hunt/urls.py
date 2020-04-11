"""jobba_hunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path, path
from django.views.generic.base import RedirectView

from jobs.views import (
    CompaniesView,
    CompanyView,
    custom_404,
    JobResponseView,
    JobView,
    MainView,
    SpecializationView,
    UserCompanyJob,
    UserCompanyVacancies,
    UserCompanyView,
    UserResumeView,
    VacanciesView,
)

handler404 = custom_404

favicon_view = RedirectView.as_view(
    url=settings.STATIC_URL + '/favicon.ico', permanent=True)

urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('jobs/<int:id>/', JobView.as_view(), name='job_detail'),
    path('jobs/cat/<str:specialization>/', SpecializationView.as_view(), name='specialization_detail'),
    path('jobs/<int:id>/send/', JobResponseView.as_view(), name='job_response'),
    path('companies/', CompaniesView.as_view(), name='companies'),
    path('companies/<int:id>/', CompanyView.as_view(), name='company_detail'),
    path('myresume/', UserResumeView.as_view(), name='user_resume'),
    path('mycompany/', UserCompanyView.as_view(), name='user_company'),
    path('mycompany/vacancies/', UserCompanyVacancies.as_view(), name='user_company_vacancies'),
    path('mycompany/vacancies/<int:id>/', UserCompanyJob.as_view(), name='user_company_job'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
