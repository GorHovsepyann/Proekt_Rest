# Generated by Django 5.0.1 on 2024-02-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_advantages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='header',
            name='name_hy',
        ),
        migrations.RemoveField(
            model_name='header',
            name='name_ru',
        ),
        migrations.AddField(
            model_name='header',
            name='page4_en',
            field=models.CharField(max_length=250, null=True, verbose_name='page4 name'),
        ),
        migrations.AddField(
            model_name='header',
            name='page4_hy',
            field=models.CharField(max_length=250, null=True, verbose_name='page4 name'),
        ),
        migrations.AddField(
            model_name='header',
            name='page4_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='page4 name'),
        ),
    ]
