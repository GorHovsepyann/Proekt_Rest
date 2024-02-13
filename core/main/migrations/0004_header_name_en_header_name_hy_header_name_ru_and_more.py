# Generated by Django 5.0.1 on 2024-01-16 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_header_page4'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='name_en',
            field=models.CharField(max_length=250, null=True, verbose_name='header name'),
        ),
        migrations.AddField(
            model_name='header',
            name='name_hy',
            field=models.CharField(max_length=250, null=True, verbose_name='header name'),
        ),
        migrations.AddField(
            model_name='header',
            name='name_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='header name'),
        ),
        migrations.AddField(
            model_name='header',
            name='page1_en',
            field=models.CharField(max_length=250, null=True, verbose_name='page1 name'),
        ),
        migrations.AddField(
            model_name='header',
            name='page1_hy',
            field=models.CharField(max_length=250, null=True, verbose_name='page1 name'),
        ),
        migrations.AddField(
            model_name='header',
            name='page1_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='page1 name'),
        ),
    ]