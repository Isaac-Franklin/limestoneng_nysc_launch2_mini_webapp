# Generated by Django 5.1.2 on 2024-10-19 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboardingapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='launchregistrants',
            name='referercode',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
