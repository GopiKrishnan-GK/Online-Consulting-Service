# Generated by Django 4.1.7 on 2023-04-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0007_alter_house_maintan_sqft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_sales',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
