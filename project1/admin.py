from django.contrib import admin
from . import  models
# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Employee)
admin.site.register(models.House_maintan)
admin.site.register(models.House_sales)
admin.site.register(models.emp_orders)
admin.site.register(models.land_sales)
admin.site.register(models.customer_orders)
admin.site.register(models.Favourite)