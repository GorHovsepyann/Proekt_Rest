# Generated by Django 5.0.1 on 2024-01-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_header_delete_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='page4',
            field=models.CharField(default=1, max_length=250, verbose_name='page4 name'),
            preserve_default=False,
        ),
    ]