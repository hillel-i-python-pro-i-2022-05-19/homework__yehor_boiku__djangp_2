# Generated by Django 4.0.5 on 2022-07-19 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(help_text='Tag for your contact', max_length=50, verbose_name='Tag')),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.CharField(default='01/01/99', max_length=20, verbose_name='Day of birth'),
        ),
        migrations.AddField(
            model_name='contact',
            name='tags',
            field=models.CharField(blank=True, choices=[('family', '#family'), ('friend', '#friend'), ('work', '#work')], default='work', help_text='Tags dor you Contact', max_length=100, verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_name',
            field=models.CharField(default='Vasya', help_text='It is name of human', max_length=20, verbose_name='Contact Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.PositiveIntegerField(help_text='Phone number must start "380"', verbose_name='Phone Number'),
        ),
        migrations.CreateModel(
            name='DetailForContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(blank=True, choices=[('APN', 'Additional phone number'), ('LinIn', 'Linkedin'), ('TG', 'Telegram'), ('EMAIL', 'Email')], default='LinIn', help_text='Add details about you Contact', max_length=100, verbose_name='Details')),
                ('detail_for_contact_type', models.CharField(default='@example', max_length=20, verbose_name='Detail for contact type')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.contact')),
            ],
        ),
    ]