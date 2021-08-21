# Generated by Django 3.2.6 on 2021-08-21 00:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=180)),
                ('message', models.TextField()),
                ('date_received', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
