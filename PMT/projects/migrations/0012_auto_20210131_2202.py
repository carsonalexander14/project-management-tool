# Generated by Django 3.0.3 on 2021-02-01 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20210131_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='positions',
            field=models.ManyToManyField(related_name='positions', to='projects.Position'),
        ),
    ]