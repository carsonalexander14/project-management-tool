# Generated by Django 3.0.3 on 2021-01-21 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
