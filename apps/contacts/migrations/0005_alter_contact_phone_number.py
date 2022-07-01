# Generated by Django 4.0.5 on 2022-06-28 19:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contacts', '0004_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxLengthValidator(15)],
                                              verbose_name='Phone Number'),
        ),
    ]
