# Generated by Django 3.0.4 on 2020-04-15 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('jobs', '0002_auto_20200415_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies',
                                    to='jobs.Specialty'),
        ),
    ]
