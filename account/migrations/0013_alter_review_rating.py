# Generated by Django 4.2.6 on 2023-11-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_remove_user_bosh_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(5, '⭐⭐⭐⭐⭐'), (1, '⭐'), (3, '⭐⭐⭐'), (2, '⭐⭐'), (4, '⭐⭐⭐⭐')], null=True),
        ),
    ]
