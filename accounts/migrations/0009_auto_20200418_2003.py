# Generated by Django 3.0.4 on 2020-04-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200418_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='resume',
            name='portfolio',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.PositiveIntegerField(default=0),
        ),
    ]