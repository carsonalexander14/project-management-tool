# Generated by Django 3.0.3 on 2020-03-18 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200310_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='display_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='display_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]