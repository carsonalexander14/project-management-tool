# Generated by Django 3.0.3 on 2021-01-29 02:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20210125_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
    ]