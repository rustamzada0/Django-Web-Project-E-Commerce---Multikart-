# Generated by Django 4.2.6 on 2023-11-11 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_category_parent'),
        ('payment', '0003_alter_billing_created_at_alter_billing_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('orderId', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('first_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('flat', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('zip', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('country', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('city', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('region', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('payed', models.IntegerField()),
                ('is_success', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Billing',
        ),
    ]
