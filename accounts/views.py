from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponse
from django.views import View
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser


class JobResponseView(View):
    template_name = "accounts/job_response.html"

    def get(self, request):
        return HttpResponse(self.template_name)


class UserResumeView(View):
    template_name = "accounts/user_resume.html"

    def get(self, request):
        return HttpResponse(self.template_name)


class UserCompanyView(View):
    template_name = "accounts/user_company.html"

    def get(self, request):
        return HttpResponse(self.template_name)


class UserCompanyVacancies(View):
    template_name = "accounts/user_company_vacancies.html"

    def get(self, request):
        return HttpResponse(self.template_name)


class UserCompanyJob(View):
    template_name = "accounts/user_company_job.html"

    def get(self, request, id: int):
        return HttpResponse(self.template_name)


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
