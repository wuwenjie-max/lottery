# Generated by Django 4.0.6 on 2022-07-28 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biglotto',
            name='blue_one',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='biglotto',
            name='blue_two',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='biglotto',
            name='number_five',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='biglotto',
            name='number_four',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='biglotto',
            name='number_one',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='biglotto',
            name='number_three',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='biglotto',
            name='number_two',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='twocolorball',
            name='number_blue',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='twocolorball',
            name='number_five',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='twocolorball',
            name='number_four',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='twocolorball',
            name='number_one',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='twocolorball',
            name='number_six',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='twocolorball',
            name='number_three',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='twocolorball',
            name='number_two',
            field=models.IntegerField(),
        ),
    ]
