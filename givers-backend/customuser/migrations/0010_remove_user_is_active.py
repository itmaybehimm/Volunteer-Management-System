# Generated by Django 3.2.4 on 2021-07-18 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0009_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
    ]