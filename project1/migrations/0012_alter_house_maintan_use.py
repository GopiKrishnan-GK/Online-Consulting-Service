# Generated by Django 4.1.7 on 2023-04-09 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0011_house_maintan_description_house_sales_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house_maintan',
            name='use',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
