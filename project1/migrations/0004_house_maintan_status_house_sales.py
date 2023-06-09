# Generated by Django 4.1.7 on 2023-03-27 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0003_house_maintan'),
    ]

    operations = [
        migrations.AddField(
            model_name='house_maintan',
            name='status',
            field=models.CharField(choices=[('Submited', 'Submited'), ('Under Verification', 'Under Verification'), ('Processing', 'Processing'), ('Under Maintanance', 'Under Maintanance'), ('Order Cancled', 'Order Cancled')], default=('Submited', 'Submited'), max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='House_sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sqft', models.PositiveIntegerField()),
                ('pub_date', models.DateField(auto_now_add=True, null=True)),
                ('specification', models.CharField(choices=[('1BHK', '1BHK'), ('2BHK', '2BHK'), ('3BHK', '3BHK'), ('4BHK', '4BHK'), ('5BHK', '5BHK')], max_length=50, null=True)),
                ('regin', models.CharField(choices=[('Madurai North', 'Madurai North'), ('Madurai South', 'Madurai South'), ('Madurai East', 'Madurai East'), ('Madurai West', 'Madurai West'), ('Madurai Central', 'Madurai Central')], max_length=50, null=True)),
                ('location', models.CharField(choices=[('Rural', 'Rural'), ('Urban', 'Urban')], max_length=50, null=True)),
                ('price', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Submited', 'Submited'), ('Under Verification', 'Under Verification'), ('Processing', 'Processing'), ('Found Buyer', 'Found Buyer'), ('Sold', 'Sold'), ('Order Cancled', 'Order Cancled')], default=('Submited', 'Submited'), max_length=100, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project1.customer')),
            ],
        ),
    ]
