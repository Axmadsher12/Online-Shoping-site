# Generated by Django 4.0.6 on 2022-08-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0012_rename_product_i_appliances_product_information_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
