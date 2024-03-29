# Generated by Django 5.0.2 on 2024-03-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_choice_act_car_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='cost_name',
            field=models.CharField(max_length=250, verbose_name='cost_atribut name'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='cost_name_en',
            field=models.CharField(max_length=250, null=True, verbose_name='cost_atribut name'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='cost_name_hy',
            field=models.CharField(max_length=250, null=True, verbose_name='cost_atribut name'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='cost_name_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='cost_atribut name'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='cost_num',
            field=models.IntegerField(verbose_name='cost_atribut price'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='spet_about',
            field=models.CharField(max_length=250, verbose_name='spet_atribut about'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='spet_about_en',
            field=models.CharField(max_length=250, null=True, verbose_name='spet_atribut about'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='spet_about_hy',
            field=models.CharField(max_length=250, null=True, verbose_name='spet_atribut about'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='spet_about_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='spet_atribut about'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='spet_name',
            field=models.CharField(max_length=250, verbose_name='spet_atribut name'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='spet_name_en',
            field=models.CharField(max_length=250, null=True, verbose_name='spet_atribut name'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='spet_name_hy',
            field=models.CharField(max_length=250, null=True, verbose_name='spet_atribut name'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='spet_name_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='spet_atribut name'),
        ),
    ]
