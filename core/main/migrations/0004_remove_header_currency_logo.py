# Generated by Django 5.0.2 on 2024-03-08 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='currency_logo',
        ),
    ]
