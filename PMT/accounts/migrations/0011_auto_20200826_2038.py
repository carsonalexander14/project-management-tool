# Generated by Django 3.0.3 on 2020-08-27 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200825_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='default_avatar.png', upload_to='profile_avatar'),
        ),
    ]
