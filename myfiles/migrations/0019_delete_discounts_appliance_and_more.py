# Generated by Django 4.0.6 on 2022-08-30 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0018_meetourteam_facebook_meetourteam_google_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Discounts_appliance',
        ),
        migrations.DeleteModel(
            name='Discounts_compyuter',
        ),
    ]