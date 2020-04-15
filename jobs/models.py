from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.URLField(max_length=128,
                              default=None,
                              null=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.URLField(max_length=128,
                           default=None,
                           null=True)
    description = models.CharField(max_length=256)
    employee_count = models.PositiveIntegerField()

    owner = models.OneToOneField('accounts.CustomUser',
                                 on_delete=models.CASCADE,
                                 related_name='company',
                                 default=None,
                                 null=True)

    def __str__(self):
        return self.name


class Skills(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty,
                                  on_delete=models.CASCADE,
                                  related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.ManyToManyField(Skills, related_name='vacancies')
    description = models.CharField(max_length=256)
    salary_min = models.PositiveIntegerField()
    salary_max = models.PositiveIntegerField()
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}  <{}>'.format(self.title, self.company)
