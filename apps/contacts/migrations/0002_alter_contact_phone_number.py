# Generated by Django 4.0.5 on 2022-06-28 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.IntegerField(verbose_name='Phone Number'),
        ),
    ]
