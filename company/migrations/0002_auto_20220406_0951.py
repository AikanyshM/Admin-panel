# Generated by Django 3.2 on 2022-04-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='appartment_number_per_floor',
            new_name='apartment_number_per_floor',
        ),
        migrations.AlterField(
            model_name='block',
            name='block_number',
            field=models.CharField(max_length=5),
        ),
    ]