# Generated by Django 4.0.6 on 2022-08-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0017_rename_appliances_appliance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetourteam',
            name='Facebook',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='meetourteam',
            name='Google',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='meetourteam',
            name='Pinterest',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='meetourteam',
            name='Twitter',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]