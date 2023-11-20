# Generated by Django 4.2.6 on 2023-11-17 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_variant_is_main_image'),
        ('payment', '0009_alter_cartitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='product.size'),
        ),
    ]
