from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from phone_field import PhoneField

from accounts.manage import CustomUserManager
from jobs.models import Specialty, Vacancy


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=128, blank=False, null=False)
    last_name = models.CharField(max_length=128, blank=False, null=False)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)


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

    # Delete default and null later
    owner = models.OneToOneField(CustomUser,
                                 on_delete=models.CASCADE,
                                 related_name='resume')
    status = models.CharField(
        max_length=24,
        choices=Status_ready_to_work.choices,
        default=Status_ready_to_work.NOT_SPECIFIED,
    )
    salary = models.PositiveIntegerField(default=0)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, related_name='resumes',
                                  default=None,
                                  null=True)
    grade = models.CharField(
        max_length=24,
        choices=Seniority_scale.choices,
        default=Seniority_scale.NOT_SPECIFIED,
    )
    education = models.CharField(max_length=128, blank=True)
    experience = models.CharField(max_length=256, blank=True)
    portfolio = models.CharField(max_length=256, blank=True)

    def get_short_name(self):
        return self.owner.first_name

    def get_full_name(self):
        return self.owner.get_full_name

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.specialty)


class Application(models.Model):
    full_name = models.CharField(max_length=64)
    phone_number = PhoneField(help_text='Contact phone number')
    written_cover_letter = models.CharField(max_length=256, blank=True)
    vacancy = models.ForeignKey(Vacancy,
                                on_delete=models.CASCADE,
                                related_name='applications')
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             related_name='applications',
                             default=None,
                             null=True)

    def __str__(self):
        return '{} <{}>'.format(self.full_name, self.phone_number)
