# Generated by Django 4.1.7 on 2023-04-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0006_house_maintan_address_house_maintan_rent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_maintan',
            name='sqft',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
