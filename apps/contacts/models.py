from django.core.validators import MaxLengthValidator
from django.db import models

from django.db.models import Field


class TagsChoices(models.TextChoices):
    FAMILY = 'family', '#family'
    FRIEND = 'friend', '#friend'
    WORK = 'work', '#work'


class Contact(models.Model):
    contact_name = models.CharField('Contact Name',
                                    help_text='It is name of human',
                                    max_length=20,
                                    default='Vasya')
    phone_number = models.PositiveIntegerField('Phone Number', help_text='Phone number must start "380"')

    birthday = models.CharField('Day of birth', max_length=20, default='01/01/99')

    tags = models.CharField(
        'Tags', max_length=100,
        help_text='Tags dor you Contact',
        choices=TagsChoices.choices,
        default=TagsChoices.WORK,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.contact_name} - {self.phone_number}'

    __repr__ = __str__


class Tags(models.Model):
    tag = models.CharField('Tag',
                           max_length=50,
                           help_text='Tag for your contact')

    def __str__(self) -> str:
        return f'{self.tag}'

    __repr__ = __str__


class DetailForContact(models.Model):
    ADDITIONAL_PHONE_NUMBER = 'APN'
    LINKEDIN = 'LinIn'
    TELEGRAM = 'TG'
    EMAIL = 'EMAIL'
    DETAIL_IN_CONTACT_CHOICES = [
        (ADDITIONAL_PHONE_NUMBER, 'Additional phone number'),
        (LINKEDIN, 'Linkedin'),
        (TELEGRAM, 'Telegram'),
        (EMAIL, 'Email'),
    ]
    contact_type = models.CharField(
        'Details',
        max_length=100,
        help_text='Add details about you Contact',
        choices=DETAIL_IN_CONTACT_CHOICES,
        default=LINKEDIN,
        blank=True,
    )
    detail_for_contact_type = models.CharField(
        'Detail for contact type',
        max_length=20,
        default='@example')

    detail = models.ForeignKey(
        to=Contact,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

######################################################
# class DetailForContact(models.Model):
#     linkedin_profile = models.CharField(
#         'LinkedIn', max_length=100,
#         help_text='Here is LinkedIn page',
#         blank='True'
#     )
#     telegram_id = models.CharField(
#         'Telegram', max_length=100,
#         help_text='Here is Telegram contact',
#         blank='True'
#     )
#     email = models.EmailField(
#         'Email', max_length=100,
#         help_text='It is email address',
#         default='example@domen.com',
#         blank=True
#     )
#
#     detail = models.ForeignKey(
#         to=Contact,
#         on_delete=models.CASCADE,
#         null=False,
#         blank=False,
#     )
#
#     def __str__(self) -> str:
#         return f'{self.linkedin_profile} ' \
#                f'- {self.telegram_id} ' \
#                f'- {self.email}'
#
#     __repr__ = __str__
