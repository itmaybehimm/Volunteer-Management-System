# Generated by Django 3.2.5 on 2021-08-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation', '0002_alter_invitation_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]