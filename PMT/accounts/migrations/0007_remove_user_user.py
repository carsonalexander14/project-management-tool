# Generated by Django 3.0.3 on 2020-03-21 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200321_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
    ]
