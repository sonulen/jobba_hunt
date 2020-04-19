from django.db import models
from django.conf import settings


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.ImageField(upload_to=settings.MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # для удаления нам нужен объект стораджа, где хранится файл с аватаркой и его путь
        self.picture.storage.delete(self.picture.path)
        super(Specialty, self).delete(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField(upload_to=settings.MEDIA_COMPANY_IMAGE_DIR)
    description = models.CharField(max_length=256)
    employee_count = models.PositiveIntegerField()

    owner = models.OneToOneField('accounts.CustomUser',
                                 on_delete=models.CASCADE,
                                 related_name='company',
                                 default=None,
                                 null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # для удаления нам нужен объект стораджа, где хранится файл с аватаркой и его путь
        self.logo.storage.delete(self.logo.path)
        super(Company, self).delete(*args, **kwargs)


class Skill(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty,
                                  on_delete=models.CASCADE,
                                  related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.ManyToManyField(Skill, related_name='vacancies')
    description = models.CharField(max_length=256)
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}  <{}>'.format(self.title, self.company)
