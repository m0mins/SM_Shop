# Generated by Django 3.2.22 on 2023-11-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address_2',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
