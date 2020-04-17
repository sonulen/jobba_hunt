from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import re_path, path
from django.views.generic.base import RedirectView

from accounts.views import (
    JobResponseView,
    UserCompanyJob,
    UserCompanyVacancies,
    UserCompanyView,
    UserResumeView,
    MyLoginView,
    MySignupView
)
from jobs.views import (
    CompaniesView,
    CompanyView,
    custom_404,
    JobView,
    MainView,
    SpecializationView,
    VacanciesView,
)

handler404 = custom_404

favicon_view = RedirectView.as_view(
    url=settings.STATIC_URL + '/favicon.ico', permanent=True)


urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', MySignupView.as_view(), name='signup'),
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
