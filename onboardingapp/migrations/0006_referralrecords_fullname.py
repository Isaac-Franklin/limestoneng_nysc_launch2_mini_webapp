# Generated by Django 5.1.2 on 2024-10-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onboardingapp', '0005_referralrecords_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='referralrecords',
            name='fullname',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
