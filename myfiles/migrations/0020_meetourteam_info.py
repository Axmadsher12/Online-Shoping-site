# Generated by Django 4.0.6 on 2022-08-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0019_delete_discounts_appliance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetourteam',
            name='Info',
            field=models.TextField(blank=True, null=True),
        ),
    ]