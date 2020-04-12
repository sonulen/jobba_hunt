from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.manage import CustomUserManager
from jobs.models import Company, Specialty


class Resume(models.Model):
    class Seniority_scale(models.TextChoices):
        NOT_SPECIFIED = 'EMPTY', _('Не указано')
        TRAINEE = 'TR', _('Стажер')
        JUNIOR = 'JUN', _('Джуниор')
        MIDDLE = 'MDL', _('Миддл')
        SENIOR = 'SNR', _('Синьор')
        LEAD = 'LD', _('Лид')

    class Status_ready_to_work(models.TextChoices):
        NOT_SPECIFIED = 'EMPTY', _('Не указано')
        NOT_LOOKING_FOR = 'NLF', _('Не ищу работу')
        CONSIDERING_OFFERS = 'CO', _('Рассматриваю предложения')
        LOOKING = 'LK', _('Ищу работу')

    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    status = models.CharField(
        max_length=24,
        choices=Status_ready_to_work.choices,
        default=Status_ready_to_work.NOT_SPECIFIED,
    )
    salary = models.PositiveIntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, related_name='resumes',
                                  default=None,
                                  null=True)
    grade = models.CharField(
        max_length=24,
        choices=Seniority_scale.choices,
        default=Seniority_scale.NOT_SPECIFIED,
    )
    education = models.CharField(max_length=128)
    experience = models.CharField(max_length=256)
    portfolio = models.CharField(max_length=256)

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    email = models.EmailField(_('email address'), unique=True)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='owner',
                                   default=None,
                                   null=True)
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name='owner',
                                  default=None,
                                  null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
