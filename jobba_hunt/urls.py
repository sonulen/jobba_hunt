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
    MainPageView,
    VacanciesPageView,
    SpecializationPageView,
    CompanyPageView,
    JobPageView
)

from jobs.views import (
    custom_404
)

favicon_view = RedirectView.as_view(
    url=settings.STATIC_URL + '/favicon.ico', permanent=True)


urlpatterns = [
    re_path(r'^favicon\.ico$', favicon_view),
    path('', MainPageView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('vacancies/', VacanciesPageView.as_view(), name='vacancies'),
    path('jobs/cat/<str:specialization>/', SpecializationPageView.as_view(), name='specialization_detail'),
    path('companies/<int:id>/', CompanyPageView.as_view(), name='company_detail'),
    path('jobs/<int:id>/', JobPageView.as_view(), name='job_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
