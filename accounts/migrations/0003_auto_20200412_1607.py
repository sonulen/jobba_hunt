# Generated by Django 3.0.4 on 2020-04-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_auto_20200412_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default='default_fn', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default='default_ln', max_length=128),
            preserve_default=False,
        ),
    ]
