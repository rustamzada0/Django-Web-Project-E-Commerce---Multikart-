# Generated by Django 4.2.6 on 2023-11-15 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bosh',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(5, '⭐⭐⭐⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (2, '⭐⭐'), (1, '⭐')], null=True),
        ),
    ]
