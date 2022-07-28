# Generated by Django 4.0.6 on 2022-07-28 07:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwoColorBall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_one', models.IntegerField(max_length=3)),
                ('number_two', models.IntegerField(max_length=3)),
                ('number_three', models.IntegerField(max_length=3)),
                ('number_four', models.IntegerField(max_length=3)),
                ('number_five', models.IntegerField(max_length=3)),
                ('number_six', models.IntegerField(max_length=3)),
                ('number_blue', models.IntegerField(max_length=3)),
                ('data_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='最后更新时间')),
            ],
            options={
                'unique_together': {('data_time',)},
            },
        ),
        migrations.CreateModel(
            name='BigLotto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_one', models.IntegerField(max_length=3)),
                ('number_two', models.IntegerField(max_length=3)),
                ('number_three', models.IntegerField(max_length=3)),
                ('number_four', models.IntegerField(max_length=3)),
                ('number_five', models.IntegerField(max_length=3)),
                ('blue_one', models.IntegerField(max_length=3)),
                ('blue_two', models.IntegerField(max_length=3)),
                ('data_time', models.DateTimeField()),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='最后更新时间')),
            ],
            options={
                'unique_together': {('data_time',)},
            },
        ),
    ]