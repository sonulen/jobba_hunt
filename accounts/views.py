from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponse
from django.views import View
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from accounts.forms import CustomUserCreationForm, ApplicationForm, ResumeForm
from accounts.models import CustomUser, Application, Resume
from jobs.forms import CompanyForm, VacancyForm
from jobs.models import Vacancy, Company, Specialty


class JobResponseView(View):
    template_name = "accounts/job_response.html"

    def create_if_new(self, request, vacancy, data):
        application = Application.objects.filter(
            full_name=data['full_name'],
            phone_number=data['phone_number'],
            written_cover_letter=data['written_cover_letter'],
            vacancy=vacancy,
            user=request.user,
        ).first()

        if application is None:
            Application.objects.create(
                full_name=data['full_name'],
                phone_number=data['phone_number'],
                written_cover_letter=data['written_cover_letter'],
                vacancy=vacancy,
                user=request.user,
            )

    def post(self, request, *args, **kwargs):
        post_data = ApplicationForm(data=request.POST)
        job_id = self.kwargs['id']

        if post_data.is_valid():
            data = post_data.cleaned_data
            vacancy = Vacancy.objects.filter(pk=job_id).first()
            self.create_if_new(request, vacancy, data)
            return render(request, self.template_name, {
                'user_name': request.user.get_full_name(),
                'back_url': reverse('job_detail', args=(job_id,))
            })

        return render(request, reverse('job_detail', args=(job_id,)),
                      {'form': post_data})


class UserResumeEmptyView(View):
    template_name = "accounts/resume_empty.html"

    @method_decorator(login_required)
    def get(self, request):
        if hasattr(request.user, 'resume'):
            return redirect('user_resume_edit')

        return render(
            request,
            self.template_name,
            context={
            }
        )


class UserResumeCreateView(View):
    template_name = "accounts/resume_create.html"

    @method_decorator(login_required)
    def get(self, request):
        if hasattr(request.user, 'resume'):
            return redirect('user_resume_edit')

        return render(
            request,
            self.template_name,
            context={
                "form": ResumeForm()
            }
        )

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if hasattr(request.user, 'resume'):
            return redirect('user_resume_edit')

        post_data = ResumeForm(data=request.POST)

        if post_data.is_valid():
            data = post_data.cleaned_data
            resume = Resume.objects.create(
                owner=request.user,
                status=data['status'],
                salary=data['salary'],
                specialty=data['specialty'],
                grade=data['grade'],
                education=data['education'],
                experience=data['experience'],
                portfolio=data['portfolio'],
            )

            return redirect('user_resume_edit')

        return render(request, self.template_name, {'form': post_data})


class UserResumeEditView(View):
    template_name = "accounts/resume_edit.html"

    @method_decorator(login_required)
    def get(self, request):
        if not hasattr(request.user, 'resume'):
            return redirect('user_resume')

        resume = request.user.resume
        form = ResumeForm(initial={
            'status': resume.status,
            'salary': resume.salary,
            'specialty': resume.specialty,
            'grade': resume.grade,
            'education': resume.education,
            'experience': resume.experience,
            'portfolio': resume.portfolio,
        })

        return render(
            request,
            self.template_name,
            context={
                'form': form
            }
        )

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if not hasattr(request.user, 'resume'):
            return redirect('user_resume')

        post_data = ResumeForm(data=request.POST)

        if post_data.is_valid():
            data = post_data.cleaned_data
            resume = request.user.resume
            resume.status = data['status']
            resume.salary = data['salary']
            resume.specialty = data['specialty']
            resume.grade = data['grade']
            resume.education = data['education']
            resume.experience = data['experience']
            resume.portfolio = data['portfolio']
            resume.save()

        return render(
            request,
            self.template_name,
            context={
                'form': post_data,
                'updated': True
            }
        )


class UserResumeDelete(View):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if not hasattr(request.user, 'resume'):
            return redirect('user_resume')

        request.user.resume.delete()

        return redirect('user_resume')


class UserCompanyEmptyView(View):
    template_name = "accounts/user_company_empty.html"

    @method_decorator(login_required)
    def get(self, request):
        if hasattr(request.user, 'company'):
            return redirect('user_company_edit')

        return render(
            request,
            self.template_name,
            context={
            }
        )


class UserCompanyCreateView(View):
    template_name = "accounts/user_company_create.html"

    @method_decorator(login_required)
    def get(self, request):
        if hasattr(request.user, 'company'):
            return redirect('user_company_edit')

        return render(
            request,
            self.template_name,
            context={
                'form': CompanyForm()
            }
        )

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if hasattr(request.user, 'company'):
            return redirect('user_company_edit')

        post_data = CompanyForm(request.POST, request.FILES)

        if post_data.is_valid():
            data = post_data.cleaned_data

            Company.objects.create(
                name=data['name'],
                location=data['location'],
                logo=data['logo'],
                description=data['description'],
                employee_count=data['employee_count'],
                owner=request.user,
            )

            return redirect('user_company_edit')

        return render(request, self.template_name, {'form': post_data})


class UserCompanyEditView(View):
    template_name = "accounts/user_company_edit.html"

    @method_decorator(login_required)
    def get(self, request):
        if not hasattr(request.user, 'company'):
            return redirect('user_company')

        company = request.user.company
        form = CompanyForm(initial={
            'name': company.name,
            'location': company.location,
            'logo': company.logo,
            'description': company.description,
            'employee_count': company.employee_count,
        })

        return render(
            request,
            self.template_name,
            context={
                'form': form,
                'logo_url': company.logo.url
            }
        )

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if not hasattr(request.user, 'company'):
            return redirect('user_company')

        post_data = CompanyForm(request.POST, request.FILES)

        if post_data.is_valid():
            data = post_data.cleaned_data
            company = request.user.company
            company.name = data['name']
            company.location = data['location']
            company.logo = data['logo']
            company.description = data['description']
            company.employee_count = data['employee_count']
            company.save()

            return render(
                request,
                self.template_name,
                context={
                    'form': post_data,
                    'logo_url': company.logo.url,
                    'updated': True
                }
            )

        return render(
            request,
            self.template_name,
            context={
                'form': post_data,
            }
        )


class UserCompanyDelete(View):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if not hasattr(request.user, 'company'):
            return redirect('user_company')

        request.user.company.delete()

        return redirect('user_company')


class UserCompanyVacancies(View):
    template_name = "accounts/user_company_vacancy_list.html"

    @method_decorator(login_required)
    def get(self, request):

        vacancies = request.user.company.vacancies

        return render(
            request,
            self.template_name,
            context={
                'company': request.user.company,
                'vacancies': vacancies.all()
            }
        )


class UserCompanyEditJob(View):
    template_name = "accounts/user_company_vacancy_edit.html"

    @method_decorator(login_required)
    def get(self, request, id: int):
        vacancy = Vacancy.objects.filter(pk=id).first()

        form = VacancyForm(initial={
            'title': vacancy.title,
            'specialty': vacancy.specialty,
            'company': vacancy.company,
            'skills': vacancy.skills,
            'description': vacancy.description,
            'salary_min': vacancy.salary_min,
            'salary_max': vacancy.salary_max,
        })

        return render(
            request,
            self.template_name,
            context={
                'vacancy_id': id,
                'company': request.user.company,
                'applications': vacancy.applications.all(),
                'form': form,
            }
        )

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        post_data = VacancyForm(request.POST)

        vacancy_pk = self.kwargs['id']
        vacancy = Vacancy.objects.filter(pk=vacancy_pk).first()

        if post_data.is_valid():
            data = post_data.cleaned_data
            vacancy.title = data['title']
            vacancy.specialty = Specialty.objects.filter(title=data['specialty']).first()
            vacancy.description = data['description']
            vacancy.salary_min = data['salary_min']
            vacancy.salary_max = data['salary_max']
            vacancy.save()

            return render(
                request,
                self.template_name,
                context={
                    'vacancy_id': vacancy_pk,
                    'form': post_data,
                    'updated': True
                }
            )

        return render(
            request,
            self.template_name,
            context={
                'vacancy_id': vacancy_pk,
                'form': post_data,
            }
        )


class UserCompanyCreateJob(View):
    template_name = "accounts/user_company_vacancy_create.html"

    @method_decorator(login_required)
    def get(self, request):

        return render(
            request,
            self.template_name,
            context={
                'form': VacancyForm(),
            }
        )

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if not hasattr(request.user, 'company'):
            return redirect('user_company')

        post_data = VacancyForm(request.POST)

        if post_data.is_valid():
            data = post_data.cleaned_data

            Vacancy.objects.create(
                title=data['title'],
                specialty=data['specialty'],
                company=request.user.company,
                description=data['description'],
                salary_min=data['salary_min'],
                salary_max=data['salary_max'],
            )

            return redirect('user_company_vacancies')

        return render(request, self.template_name, {'form': post_data})


class UserCompanyDeleteJob(View):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        vacancy_pk = self.kwargs['id']

        Vacancy.objects.filter(pk=vacancy_pk).delete()

        return redirect('user_company_vacancies')


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'

    def post(self, request, *args, **kwargs):
        post_data = AuthenticationForm(data=request.POST)

        if post_data.is_valid():
            data = post_data.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                post_data.add_error(None, 'User cannot be found')
                return render(request, self.template_name, {'form': post_data})

        else:
            if 'username' not in post_data.cleaned_data:
                post_data.add_error('email', 'Invalid email')
            if 'password' not in post_data.cleaned_data:
                post_data.add_error('password', 'Invalid password')

            return render(request, self.template_name, {'form': post_data})


class MySignupView(CreateView):
    redirect_authenticated_user = True
    form_class = CustomUserCreationForm
    success_url = 'login'
    template_name = 'accounts/signup.html'

    def post(self, request, *args, **kwargs):
        post_data = CustomUserCreationForm(data=request.POST)

        if post_data.is_valid():
            data = post_data.cleaned_data

            email = data['email']
            password = data['password1']
            first_name = data['first_name']
            last_name = data['last_name']
            user = CustomUser.objects.create_user(email=email, password=password,
                                                  first_name=first_name, last_name=last_name)
            user.save()
            return redirect('login')

        return render(request, self.template_name, {'form': post_data})
