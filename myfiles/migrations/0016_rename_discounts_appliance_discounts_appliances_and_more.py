# Generated by Django 4.0.6 on 2022-08-21 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0015_delete_ffff'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Discounts_appliance',
            new_name='Discounts_appliances',
        ),
        migrations.RenameModel(
            old_name='type_appliance',
            new_name='type_appliances',
        ),
    ]