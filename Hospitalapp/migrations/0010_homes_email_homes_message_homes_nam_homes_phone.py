# Generated by Django 5.0.3 on 2024-03-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0009_alter_package_ln10_alter_package_ln11_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homes',
            name='email',
            field=models.CharField(default=0.09090909090909091, max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homes',
            name='message',
            field=models.CharField(default=12, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homes',
            name='nam',
            field=models.CharField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homes',
            name='phone',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
