
from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.index,name='index-page'),
    path('customer-home',views.customer_home ,name='customer-home'),
    path('employee-home',views.employee_home ,name='employee-home'),
    path('admin-home',views.admin_home ,name='admin-home'),
    
    path('customerlogin', LoginView.as_view(template_name='customerlogin.html'),name='customerlogin'),
    path('employeelogin', LoginView.as_view(template_name='employeelogin.html'),name='employeelogin'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html'),name='adminlogin'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('housemaintain',views.customer_addhouse_maintanance,name='housemaintain'),
    path('customersignup',views.customer_signup_view,name='customersignup'),
    path('employeesignup',views.employee_signup_view,name='employeesignup'),
    path('house-maintan',views.house_maintan,name='house-maintan'),
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),
    path('housedetails/<int:pk>', views.renthouse_details,name='housedetails'),
    path('housesalesdetails/<int:pk>', views.housesales_details,name='housesalesdetails'),
    path('landsalesdetails/<int:pk>', views.landsales_details,name='landsalesdetails'),
    path('housesaleshome',views.housesales_home,name='housesaleshome'),
    path('addhousesales',views.c_add_house_sales,name='addhousesales'),
    path('housesales',views.house_sales,name='housesales'),
    path('profileclick',views.userprofile_view,name='profileclick'),
    path('customerdeleteorder/<str:m1>/<int:pk>',views.customer_delete_order,name='customerdeleteorder'),
    path('customereditorder/<str:model>/<int:pk>',views.customer_edit_order,name='customereditorder'),
    path('emphousemaintandetails/<int:id>/<str:val>',views.emphousemaintandetails,name='emphousemaintandetails'),
    path('emphousesalesdetails/<int:id>/<str:val>',views.emphousesalesdetails,name='emphousesalesdetails'),
    path('emplandsalesdetails/<int:id>/<str:val>',views.emplandsalesdetails,name='emplandsalesdetails'),
    path('landsales',views.land_saleshome,name='landsales'),
    path('addlandsale',views.add_land_sale,name='addlandsale'),
    path('landsaleslist',views.land_sales,name='landsaleslist'),
    path('employeetasks',views.employeetasks,name='employeetasks'),
    path('taskhousemaintan',views.taskhousemaintan,name='taskhouseaintan'),
    path('taskhousesales',views.taskhousesales,name='taskhousesales'),
    path('tasklandsales',views.tasklandsale,name='tasklandsales'),
    path('emporders',views.emporders,name='emporders'),
    path('customerinfo/<int:pk>', views.customerinfo,name='customerinfo'),
    path('favourite/<str:model>/<int:pk>',views.favourite,name="favourite"),
    path('favpage',views.favourite_page,name='favpage'),
    path('removefav/<int:id>',views.removefav,name='removefav'),
    path('checkstatus',views.checkstatus,name='checkstatus'),
    path('removeorder/<int:id>',views.removeorder,name='removeorder'),


]