# Generated by Django 5.0.3 on 2024-03-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0007_package_categ'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='categ',
            new_name='ln1',
        ),
        migrations.AddField(
            model_name='package',
            name='ln10',
            field=models.CharField(default=0.09090909090909091, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='ln11',
            field=models.CharField(default=0.34375, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='ln12',
            field=models.CharField(default=0.4, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='ln13',
            field=models.CharField(default=0.25, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='ln2',
            field=models.CharField(default=0.07407407407407407, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='ln3',
            field=models.CharField(default=0.1111111111111111, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='ln4',
            field=models.CharField(default=0.09876543209876543, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='ln5',
            field=models.CharField(default=0.1111111111111111, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='ln6',
            field=models.CharField(default=0.12698412698412698, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='ln7',
            field=models.CharField(default=0.12698412698412698, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='ln8',
            field=models.CharField(default=0.1875, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='ln9',
            field=models.CharField(default=0.2, max_length=400),
            preserve_default=False,
        ),
    ]
