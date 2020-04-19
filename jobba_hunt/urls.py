from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import re_path, path
from django.views.generic.base import RedirectView
from django.views.static import serve

from accounts.views import (
    JobResponseView,
    MyLoginView,
    MySignupView,
    UserCompanyCreateView,
    UserCompanyDelete,
    UserCompanyEditView,
    UserCompanyEmptyView,
    UserCompanyDeleteJob,
    UserCompanyEditJob,
    UserCompanyCreateJob,
    UserCompanyVacancies,
    UserResumeCreateView,
    UserResumeDelete,
    UserResumeEditView,
    UserResumeEmptyView,
)

from jobs.views import (
    CompaniesView,
    CompanyView,
    custom_404,
    JobView,
    MainView,
    SpecializationView,
    VacanciesView,
    VacanciesSearchView
)

handler404 = custom_404

favicon_view = RedirectView.as_view(
    url=settings.STATIC_URL + '/favicon.ico', permanent=True)


urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('companies/', CompaniesView.as_view(), name='companies'),
    path('companies/<int:id>/', CompanyView.as_view(), name='company_detail'),
    path('jobs/<int:id>/', JobView.as_view(), name='job_detail'),
    path('jobs/<int:id>/send', JobResponseView.as_view(), name='job_response'),
    path('jobs/cat/<str:specialization>/', SpecializationView.as_view(), name='specialization_detail'),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/search/<str:keyword>/', VacanciesSearchView.as_view(), name='search_vacancies'),
    path('vacancies/search/', VacanciesSearchView.as_view(), name='search_vacancies'),
    # Создание/Логин пользователя
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', MySignupView.as_view(), name='signup'),
    # Создание резюме
    path('myresume/empty/', UserResumeEmptyView.as_view(), name='user_resume'),
    path('myresume/create/', UserResumeCreateView.as_view(), name='user_resume_create'),
    path('myresume/edit/', UserResumeEditView.as_view(), name='user_resume_edit'),
    path('myresume/delete/', UserResumeDelete.as_view(), name='user_resume_delete'),
    #  Создание компании
    path('mycompany/empty/', UserCompanyEmptyView.as_view(), name='user_company'),
    path('mycompany/create/', UserCompanyCreateView.as_view(), name='user_company_create'),
    path('mycompany/edit/', UserCompanyEditView.as_view(), name='user_company_edit'),
    path('mycompany/delete/', UserCompanyDelete.as_view(), name='user_company_delete'),
    # Создание вакансий в компании пользователя
    path('mycompany/vacancies/', UserCompanyVacancies.as_view(), name='user_company_vacancies'),
    path('mycompany/vacancies/<int:id>/', UserCompanyEditJob.as_view(), name='user_company_job_edit'),
    path('mycompany/vacancies/create/', UserCompanyCreateJob.as_view(), name='user_company_job_create'),
    path('mycompany/vacancies/<int:id>/delete', UserCompanyDeleteJob.as_view(), name='user_company_job_delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# MEDIA URLS
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',
            serve,
            {'document_root': settings.MEDIA_ROOT})
]
