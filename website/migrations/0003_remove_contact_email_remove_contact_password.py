# Generated by Django 4.1.3 on 2023-01-21 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_contact_address_alter_contact_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='password',
        ),
    ]
