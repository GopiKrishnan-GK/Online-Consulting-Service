from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.username

class Employee(models.Model):
    REGIN=(('Madurai North','Madurai North'),
           ('Madurai South','Madurai South'),
           ('Madurai East','Madurai East'),
           ('Madurai West','Madurai West'),
           ('Madurai Central','Madurai Central'),
           )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/EmployeeProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    regin=models.CharField(max_length=50,null=True,choices=REGIN)
    tasks=models.IntegerField(default=0)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.username

class House_maintan(models.Model):
    SPECIFICATION=(
        ('1BHK','1BHK'),
        ('2BHK','2BHK'),
        ('3BHK','3BHK'),
       
    )
    REGIN=(
           ('Madurai North','Madurai North'),
           ('Madurai South','Madurai South'),
           ('Madurai East','Madurai East'),
           ('Madurai West','Madurai West'),
           ('Madurai Central','Madurai Central'),
           )
    loc=(
        ('Rural','Rural'),
        ('Urban','Urban'),
    )
    status1=(
        ('Submited','Submited'),
        ('Under Verification','Under Verification'),
        ('Processing','Processing'),
        ('On Rent','On Rent'),
        ('Under Maintanance','Under Maintanance'),
        ('Order Cancled','Order Cancled'),
        

    )
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,null =True)
    sqft=models.PositiveIntegerField(null=True)
    image=models.ImageField(upload_to='houseimages/',null=True,blank=True)
    pub_date=models.DateField(auto_now_add=True,null=True)
    specification=models.CharField(max_length=50,null=True,choices=SPECIFICATION)
    regin=models.CharField(max_length=50,null=True,choices=REGIN)
    location=models.CharField(max_length=50,null=True,choices=loc)
    use=models.BooleanField(null=True,default=False)
    status=models.CharField(max_length=100,null=True,choices=status1,default=status1[0][0])
    address=models.CharField(max_length=200,null=True)
    rent=models.PositiveIntegerField(null=True)
    time=models.PositiveIntegerField(null=True)
    description=models.CharField(max_length=255,null=True)


class House_sales(models.Model):
    SPECIFICATION=(
        ('1BHK','1BHK'),
        ('2BHK','2BHK'),
        ('3BHK','3BHK'),
       
    )
    REGIN=(
           ('Madurai North','Madurai North'),
           ('Madurai South','Madurai South'),
           ('Madurai East','Madurai East'),
           ('Madurai West','Madurai West'),
           ('Madurai Central','Madurai Central'),
           )
    loc=(
        ('Rural','Rural'),
        ('Urban','Urban'),
    )
    status1=(
        ('Submited','Submited'),
        ('Under Verification','Under Verification'),
        ('Processing','Processing'),
        ('Found Buyer','Found Buyer'),
        ('Sold','Sold'),
        ('Order Cancled','Order Cancled'),

    )
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,null =True)
    sqft=models.PositiveIntegerField(null=True)
    image=models.ImageField(upload_to='houseimagessales/',null=True,blank=True)
    pub_date=models.DateField(auto_now_add=True,null=True)
    specification=models.CharField(max_length=50,null=True,choices=SPECIFICATION)
    regin=models.CharField(max_length=50,null=True,choices=REGIN)
    location=models.CharField(max_length=50,null=True,choices=loc)
    address=models.CharField(max_length=300,null=True)
    price=models.PositiveIntegerField(null=True)
    status=models.CharField(max_length=100,null=True,choices=status1,default=status1[0][0])
    description=models.CharField(max_length=255,null=True)

class land_sales(models.Model):
    REGIN=(
           ('Madurai North','Madurai North'),
           ('Madurai South','Madurai South'),
           ('Madurai East','Madurai East'),
           ('Madurai West','Madurai West'),
           ('Madurai Central','Madurai Central'),
           )
    loc=(
        ('Rural','Rural'),
        ('Urban','Urban'),
    )
    status1=(
        ('Submited','Submited'),
        ('Under Verification','Under Verification'),
        ('Processing','Processing'),
        ('Found Buyer','Found Buyer'),
        ('Sold','Sold'),
        ('Order Cancled','Order Cancled'),

    )
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,null =True)
    image=models.ImageField(upload_to='landimages/',null=True,blank=True)
    address=models.CharField(max_length=500,null=True,blank=True)
    sqft=models.PositiveIntegerField(null=True)
    pub_date=models.DateField(auto_now_add=True,null=True)
    regin=models.CharField(max_length=50,null=True,choices=REGIN)
    location=models.CharField(max_length=50,null=True,choices=loc)
    price=models.PositiveIntegerField(null=True)
    status=models.CharField(max_length=100,null=True,choices=status1,default=status1[0][0])
    description=models.CharField(max_length=255,null=True)
    
class emp_orders(models.Model):

    employee=models.ForeignKey('Employee',on_delete=models.CASCADE,null=True)
    house_maintan=models.OneToOneField('House_maintan',on_delete=models.CASCADE,null=True,blank=True)
    house_sales=models.OneToOneField('House_sales',on_delete=models.CASCADE,null=True,blank=True)
    land_sales=models.OneToOneField('Land_sales',on_delete=models.CASCADE,null=True,blank=True)
    result=models.CharField(max_length=70,null=True)

class customer_orders(models.Model):
    status1=(
    ('Submited','Submited'),
    ('Processing','Processing'),
    ('Success','Success'),
    ('Order Cancled','Order Cancled') )
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,null=True)
    house_maintan=models.ForeignKey('House_maintan',on_delete=models.CASCADE,null=True,blank=True)
    house_sales=models.ForeignKey('House_sales',on_delete=models.CASCADE,null=True,blank=True)
    land_sales=models.ForeignKey('Land_sales',on_delete=models.CASCADE,null=True,blank=True)
    status=models.CharField(max_length=70,choices=status1,default=status1[0][0])
class Favourite(models.Model):
    customer=models.ForeignKey('Customer',on_delete=models.CASCADE,null=True)
    house_maintan=models.ForeignKey('House_maintan',on_delete=models.CASCADE,null=True,blank=True)
    house_sales=models.ForeignKey('House_sales',on_delete=models.CASCADE,null=True,blank=True)
    land_sales=models.ForeignKey('Land_sales',on_delete=models.CASCADE,null=True,blank=True)
