# Generated by Django 5.0.2 on 2024-03-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_slayder_background_reservation_engine_name_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slayder',
            name='button_name_en',
            field=models.CharField(max_length=250, null=True, verbose_name='button name'),
        ),
        migrations.AddField(
            model_name='slayder',
            name='button_name_hy',
            field=models.CharField(max_length=250, null=True, verbose_name='button name'),
        ),
        migrations.AddField(
            model_name='slayder',
            name='button_name_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='button name'),
        ),
    ]
