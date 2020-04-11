from django_enumfield import enum
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.manage import CustomUserManager
from jobs.models import Company, Specialty


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='user',
                                   default=None,
                                   null=True)
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name='user',
                                  default=None,
                                  null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Seniority_scale(enum.Enum):
    NOT_SPECIFIED = 0
    TRAINEE = 1
    JUNIOR = 2
    MIDDLE = 3
    SENIOR = 4
    LEAD = 5

    __labels__ = {
        NOT_SPECIFIED: "Не указано",
        TRAINEE: "Стажер",
        JUNIOR: "Джуниор",
        MIDDLE: "Миддл",
        SENIOR: "Синьор",
        LEAD: "Лид",
    }


class Status_ready_to_work(enum.Enum):
    NOT_SPECIFIED = 0
    NOT_LOOKING_FOR = 1
    CONSIDERING_OFFERS = 2
    LOOKING = 3

    __labels__ = {
        NOT_SPECIFIED: "Не указано",
        NOT_LOOKING_FOR: "Не ищу работу",
        CONSIDERING_OFFERS: "Рассматриваю предложения",
        LOOKING: "Ищу работу",
    }


class Resume(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    status = enum.EnumField(Status_ready_to_work, default=Status_ready_to_work.NOT_SPECIFIED)
    salary = models.PositiveIntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, related_name='resumes',
                                  default=None,
                                  null=True)
    grade = enum.EnumField(Seniority_scale, default=Seniority_scale.NOT_SPECIFIED)
    education = models.CharField(max_length=128)
    experience = models.CharField(max_length=64)
    portfolio = models.CharField(max_length=256)
