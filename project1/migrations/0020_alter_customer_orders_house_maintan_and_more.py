# Generated by Django 4.1.7 on 2023-04-16 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0019_employee_tasks_alter_emp_orders_house_maintan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_orders',
            name='house_maintan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project1.house_maintan'),
        ),
        migrations.AlterField(
            model_name='customer_orders',
            name='house_sales',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project1.house_sales'),
        ),
        migrations.AlterField(
            model_name='customer_orders',
            name='land_sales',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project1.land_sales'),
        ),
    ]
