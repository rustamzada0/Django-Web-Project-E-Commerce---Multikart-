# Generated by Django 4.2.6 on 2023-11-15 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(5, '⭐⭐⭐⭐⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (1, '⭐')], null=True),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
