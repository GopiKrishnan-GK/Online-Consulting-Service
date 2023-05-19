from django import forms
from django.contrib.auth.models import User
from . import models


class CreateUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile']
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=models.Employee
        fields=['address','mobile']
    

class HouseMaintananceForm(forms.ModelForm):
    
    class Meta:
        model=models.House_maintan
        
        fields=['image','sqft','specification','regin','location','address','use','time','description']
class HouseMaintananceForm1(forms.ModelForm):
    
    class Meta:
        model=models.House_maintan
        
        fields=['image','sqft','specification','regin','location','address','use','time','description','rent','status']
        labels={
            "use": 'For Rent?',
            "rent":'Rent(Estimated)',
            'sqft':'Square Feet'
        }

class HouseSalesForm(forms.ModelForm):
    class Meta:
        model=models.House_sales
        fields=['image','sqft','specification','regin','location','address','description']
class HouseSalesForm1(forms.ModelForm):
    class Meta:
        model=models.House_sales
        fields=['image','sqft','specification','regin','location','address','description','status','price']
        labels={
            'sqft':"Square Feet",
            'price':"Price(Estimated)",
        }

class LandSalesForm(forms.ModelForm):
    class Meta:
        model=models.House_sales
        fields=['image','sqft','regin','location','address','description']

class LandSalesForm1(forms.ModelForm):
    class Meta:
        model=models.House_sales
        fields=['image','sqft','regin','location','address','description','price','status'] 
        labels={
            'sqft':"Square Feet",
            'price':"Price(Estimated)",
        }
class CustomerOrdersForm(forms.ModelForm):
    id=forms.IntegerField(widget=forms.HiddenInput())
    class Meta:
        model=models.customer_orders
        fields=['status','id']
        


