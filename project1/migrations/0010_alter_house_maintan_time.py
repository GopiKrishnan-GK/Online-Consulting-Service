# Generated by Django 4.1.7 on 2023-04-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0009_alter_house_maintan_use_alter_house_sales_sqft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_maintan',
            name='time',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
