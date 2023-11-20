# Generated by Django 4.2.6 on 2023-11-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='forget_pwd_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]