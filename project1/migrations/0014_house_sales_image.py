# Generated by Django 4.1.7 on 2023-04-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0013_alter_house_maintan_status_alter_land_sales_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house_sales',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='houseimagessales/'),
        ),
    ]
