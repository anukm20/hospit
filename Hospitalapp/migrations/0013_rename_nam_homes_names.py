# Generated by Django 5.0.3 on 2024-03-24 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0012_remove_homes_phone_homes_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homes',
            old_name='nam',
            new_name='names',
        ),
    ]
