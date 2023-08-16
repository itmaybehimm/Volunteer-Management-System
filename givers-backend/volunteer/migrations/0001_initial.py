# Generated by Django 3.2.4 on 2021-07-06 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_events_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='requestevents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_details', models.ImageField(default='avatar.jpg', upload_to='request_volunteer')),
                ('description', models.CharField(max_length=2000, null=True)),
                ('interested', models.BooleanField(default=False)),
                ('request_volunteer', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='verify',
            fields=[
                ('requestevents_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='volunteer.requestevents')),
                ('org_verify', models.BooleanField(default=False)),
            ],
            bases=('volunteer.requestevents',),
        ),
    ]
