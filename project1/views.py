from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
from . import models
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django import template
# Create your views here.
def index(request):
    return render(request,'index.html')

def customer_signup_view(request):
    userForm=forms.CreateUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CreateUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=customerForm.save(commit=False)
            customer.user=user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
            messages.success(request,"You have Signed up successfully!! you can login now")
            return HttpResponseRedirect('customerlogin')
       
    return render(request,'customersignup.html',context=mydict)
@login_required(login_url='adminlogin')
def employee_signup_view(request):
    userForm=forms.CreateUserForm()
    employeeForm=forms.EmployeeForm()
    mydict={'userForm':userForm,'employeeForm':employeeForm}
    if request.method=='POST':
        userForm=forms.CreateUserForm(request.POST)
        employeeForm=forms.EmployeeForm(request.POST,request.FILES)
        if userForm.is_valid() and employeeForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            employee=employeeForm.save(commit=False)
            employee.user=user
            employee.save()
            my_employee_group = Group.objects.get_or_create(name='EMPLOYEE')
            my_employee_group[0].user_set.add(user)
        return HttpResponseRedirect('employeelogin')
    return render(request,'employeesignup.html',context=mydict)

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()
def is_employee(user):
    return user.groups.filter(name='EMPLOYEE').exists()
def afterlogin_view(request):
    
    if is_customer(request.user):
        return HttpResponseRedirect('customer-home')
    elif is_employee(request.user):
        return HttpResponseRedirect('employee-home')
    else:
        return HttpResponseRedirect('admin')

def rent_cal(specification,location,use):
    rent=0
    if use:
        
        if location=="Rural":
            if specification=="1BHK":
                rent=5000
            elif specification=="2BHK":
                rent=9000
            elif specification=="3BHK":
                rent=18000
        elif location=="Urban":
            if specification=="1BHK":
                rent=8000
            elif specification=="2BHK":
                rent=15000
            elif specification=="3BHK":
                rent=20000
    
    return rent


    
@login_required(login_url='customerlogin')
def customer_addhouse_maintanance(request):
    form=forms.HouseMaintananceForm()
    if request.user.is_authenticated:
        
        if request.method=="POST": 
            form=forms.HouseMaintananceForm(request.POST,request.FILES)
            if form.is_valid():
                customer=request.user.customer
                sqft=form.cleaned_data['sqft']
                time=form.cleaned_data['time']
                image=form.cleaned_data['image']
                specification=form.cleaned_data['specification']
                print(image)
                location=form.cleaned_data['location']
                address=form.cleaned_data['address']
                use=form.cleaned_data['use']
                regin=form.cleaned_data['regin']
                rent=rent_cal(specification,location,use)
                description=form.cleaned_data['description']
                models.House_maintan.objects.create(customer=customer,sqft=sqft,image=image,specification=specification,
                                                    regin=regin,location=location,use=use,address=address,time=time,rent=rent,description=description)
                messages.success(request,"Added Successfully")
                return render(request,'index.html')
        else:
            messages.error(request,'Failure')
            return render(request,'housemaintain.html',{'form':form})
    else:   
        return redirect('customerlogin')
    return render(request,'housemaintain.html',{'form':form})


          
    

def house_maintan(request):
    status='Processing'
    house=models.House_maintan.objects.filter(use=True,status=status)
    
    return render(request,'house-maintan.html',{'houses':house})

def renthouse_details(request,pk):
    house=models.House_maintan.objects.get(id=pk)
    if is_customer(request.user):
        if request.method=="POST":
            customer=request.user.customer
            h=models.customer_orders.objects.filter(customer=customer,house_maintan=house)
            if h:
                HttpResponse("You have already Ordered for Consultant")
            else:
                models.customer_orders.objects.create(customer=customer,house_maintan=house)
                return render(request,'afterorder.html')
    return render(request,'renthouse-details.html',{'house':house})

def housesales_details(request,pk):
    house=models.House_sales.objects.get(id=pk)
    if is_customer(request.user):
        if request.method=="POST":
            customer=request.user.customer
            h=models.customer_orders.objects.filter(customer=customer,house_sales=house)
            if h:
                HttpResponse("You have already Ordered for Consultant")
            else:
                models.customer_orders.objects.create(customer=customer,house_sales=house)
                return render(request,'afterorder.html')
    return render(request,'housesalesdetails.html',{'house':house})

def landsales_details(request,pk):
    land=models.land_sales.objects.get(id=pk)
    if is_customer(request.user):
        if request.method=="POST":
            customer=request.user.customer
            h=models.customer_orders.objects.filter(customer=customer,land_sales=land)
            if h:
                HttpResponse("You have already Ordered for Consultant")
            else:
                models.customer_orders.objects.create(customer=customer,land_sales=land)
                return render(request,'afterorder.html')
    return render(request,'landsalesdetails.html',{'land':land})
def housesales_home(request):
    return render(request,'customer_house_sales.html')

@login_required(login_url='customerlogin')
def c_add_house_sales(request):
    form=forms.HouseSalesForm()
    if request.method=='POST':
        form=forms.HouseSalesForm(request.POST,request.FILES)
        if form.is_valid():
            customer=request.user.customer
            sqft=form.cleaned_data['sqft']
            image=form.cleaned_data['image']
            specification=form.cleaned_data['specification']
            location=form.cleaned_data['location']
            address=form.cleaned_data['address']
            price=price_estimate_house(specification,location,sqft)
            regin=form.cleaned_data['regin']
            
            description=form.cleaned_data['description']
            models.House_sales.objects.create(customer=customer,image=image,sqft=sqft,specification=specification,
                                                    regin=regin,location=location,address=address,price=price,description=description)
            return redirect('customer-home')
        
    return render(request,'addhousesales.html',{'form':form})
def c_house_sales(request):
    return render(request,'customer_house_sales1.html')

def userprofile_view(request):
    if is_customer(request.user):
        return redirect('customer-home')

    elif is_employee(request.user):
        return redirect('employee-home')
    else:
        
        return redirect('admin/')
   
@login_required(login_url='customerlogin')
def customer_home(request):
    customer=models.Customer.objects.get(user=request.user)
    house=models.House_maintan.objects.filter(customer=customer)
    house_sale=models.House_sales.objects.filter(customer=customer)
    land_sale=models.land_sales.objects.filter(customer=customer)
    context={'customer':customer,'house':house, 'house_sale':house_sale,'land_sale':land_sale}

    return render(request,'customerhome.html',context)
@login_required(login_url='employeelogin')
def employee_home(request):
    emp=models.Employee.objects.get(user=request.user)
    region=emp.regin
    status='Submited'
    orders=models.House_maintan.objects.filter(regin=region,status=status)
    house_sale=models.House_sales.objects.filter(regin=region,status=status)
    land_sale=models.land_sales.objects.filter(regin=region,status=status)

    return render(request,"employeehome.html",{'employee': emp,'orders':orders,'house_sale':house_sale,'land_sale':land_sale})
@login_required(login_url='adminlogin')
def admin_home(request):
    return HttpResponseRedirect("admin")

def customer_delete_order(request,m1,pk):
    if m1=='House_maintan':
        item=models.House_maintan.objects.get(id=pk)
    elif m1=='House_sales':
        item=models.House_sales.objects.get(id=pk)
    elif m1=='land_sales':
         item=models.land_sales.objects.get(id=pk)
    item.delete()
    return redirect('customer-home')

def customer_edit_order(request,model,pk):
    if model=='House_maintan':
        itm=models.House_maintan.objects.get(id=pk)
        form=forms.HouseMaintananceForm(instance=itm)
        
        if request.method=="POST": 
            form=forms.HouseMaintananceForm(request.POST,request.FILES,instance=itm)
            if form.is_valid():
                if request.method=="POST": 
                    form.save()
                    return redirect('customer-home')
            
        return render(request,'edithousemaintan.html',{'form':form}) 
    elif model=='House_sales':
        itm=models.House_sales.objects.get(id=pk)
        form=forms.HouseSalesForm(instance=itm)
        
        if request.method=="POST": 
            form=forms.HouseSalesForm(request.POST,request.FILES,instance=itm)
            if form.is_valid():
                if request.method=="POST": 
                    form.save()
                    return redirect('customer-home')
            
        return render(request,'edithousesale.html',{'form':form})
    elif model=='land_sales':
        itm=models.land_sales.objects.get(id=pk)
        form=forms.LandSalesForm(instance=itm)
        
        if request.method=="POST": 
            form=forms.LandSalesForm(request.POST,request.FILES,instance=itm)
            if form.is_valid():
                if request.method=="POST": 
                    form.save()
                    return redirect('customer-home')
            
        return render(request,'editlandsale.html',{'form':form}) 


def price_estimate_house(specification,location,sqft):
    sqft1=0
    amount=0
    if location=='Rural':
        sqft1=3800*sqft
    elif location=='Urban':
        sqft1=4800*sqft
    if specification=="1BHK":
        amount=sqft1+100000
    elif specification=='2BHK':
        amount=sqft1+200000
    elif specification=="3BHK":
        amount=sqft1+300000
    return amount
@login_required(login_url='employeelogin')   
def emphousemaintandetails(request,id,val):
    itm=models.House_maintan.objects.get(id=id)
    form=forms.HouseMaintananceForm1(instance=itm)
    if request.method=="POST":
        form=forms.HouseMaintananceForm1(request.POST,request.FILES,instance=itm)
        if form.is_valid():
            form.save()
            employee=request.user.employee
            

            models.emp_orders.objects.get_or_create(employee=employee,house_maintan=itm)
            return redirect('employee-home')
    return render(request,'emphousemaintandetails.html',{'form':form,'house':itm,'val':val})
@login_required(login_url='employeelogin')
def emphousesalesdetails(request,id,val):
    itm=models.House_sales.objects.get(id=id)
    form=forms.HouseSalesForm1(instance=itm)
    
    if request.method=="POST":
        form=forms.HouseSalesForm1(request.POST,request.FILES,instance=itm)
        if form.is_valid():
            form.save()
            employee=request.user.employee
            

            models.emp_orders.objects.get_or_create(employee=employee,house_sales=itm)
            return redirect('employee-home')
    return render(request,'emphousesalesdetails.html',{'form':form,'house':itm,'val':val})
@login_required(login_url='employeelogin')
def emplandsalesdetails(request,id,val):
    itm=models.land_sales.objects.get(id=id)
    form=forms.LandSalesForm1(instance=itm)
    if request.method=="POST":
        form=forms.LandSalesForm1(request.POST,request.FILES,instance=itm)
        if form.is_valid():
            form.save()
            employee=request.user.employee
            

            models.emp_orders.objects.get_or_create(employee=employee,land_sales=itm)
            return redirect('employee-home')
    return render(request,'emplandsalesdetails.html',{'form':form,'house':itm,'val':val})

def land_saleshome(request):
    return render(request,'landsales.html')

def price_estimate_land(location,sqft):
    amount=0
    if location=="Rural":
        amount=1800*sqft
    elif location=="Urban":
        amount=3000*sqft
    return amount
@login_required(login_url='customerlogin')
def add_land_sale(request):
    form=forms.LandSalesForm()
    if is_customer(request.user):
        if request.method=='POST':
            form=forms.LandSalesForm(request.POST,request.FILES)
            if form.is_valid():
                customer=request.user.customer
                sqft=form.cleaned_data['sqft']
                image=form.cleaned_data['image']
                location=form.cleaned_data['location']
                address=form.cleaned_data['address']
                price=price_estimate_land(location,sqft)
                regin=form.cleaned_data['regin']
                models.land_sales.objects.create(customer=customer,sqft=sqft,image=image,location=location,
                                                 address=address,price=price,regin=regin)
                return redirect('customer-home')
    return render(request,'addlandsale.html',{'form':form})

def house_sales(request):
    status='Processing'
    house=models.House_sales.objects.filter(status=status)
    return render(request,'housesaleslist.html',{'houses':house})

def land_sales(request):
    status='Processing'
    house=models.land_sales.objects.filter(status=status)
    return render(request,'landsaleslist.html',{'houses':house})

def employeetasks(request):
    
    return render(request,'employeetasks.html')

def taskhousemaintan(request):
    employee=request.user.employee
    orders=models.emp_orders.objects.filter(employee=employee,house_maintan__isnull=False)
    return render(request,'taskhousemaintan.html',{'houses':orders})

def taskhousesales(request):
    employee=request.user.employee
    orders=models.emp_orders.objects.filter(employee=employee,house_sales__isnull=False)
    return render(request,'taskhousesales.html',{'houses':orders})

def tasklandsale(request):
    employee=request.user.employee
    orders=models.emp_orders.objects.filter(employee=employee,land_sales__isnull=False)
    return render(request,'tasklandsales.html',{'houses':orders})

def emporders(request):
    
    employee=request.user.employee
    emp1=models.emp_orders.objects.filter(employee=employee,house_maintan__isnull=False)
    cus1=models.customer_orders.objects.filter(house_maintan__isnull=False)
    orders_c1=[]
    orders_e1=[]
    for h in emp1:
        for h1 in cus1:
            if h.house_maintan.id == h1.house_maintan.id:
                orders_e1.append(h)
                orders_c1.append(h1)
    emp2=models.emp_orders.objects.filter(employee=employee,house_sales__isnull=False)
    cus2=models.customer_orders.objects.filter(house_sales__isnull=False)
    orders_c2=[]
    orders_e2=[]
    for h in emp2:
        for h1 in cus2:
            if h.house_sales.id == h1.house_sales.id:
                orders_e2.append(h)
                orders_c2.append(h1)
    emp3=models.emp_orders.objects.filter(employee=employee,land_sales__isnull=False)
    cus3=models.customer_orders.objects.filter(land_sales__isnull=False)
    orders_c3=[]
    orders_e3=[]
    for h in emp3:
        for h1 in cus3:
            if h.land_sales.id == h1.land_sales.id:
                orders_e3.append(h)
                orders_c3.append(h1)
    if request.method=="POST":
        id=request.POST.get('id')
        status=request.POST.get('status')
        models.customer_orders.objects.filter(id=id).update(status=status)

    context={'orders_c1':orders_c1,'orders_e1':orders_e1,'orders_c2':orders_c2,'orders_e2':orders_e2,
             'orders_c3':orders_c3,'orders_e3':orders_e3}
    return render(request,'emporders.html',context)
def customerinfo(request,pk):
    customer=models.Customer.objects.get(id=pk)
    print(customer)
    return render(request,'customerinfo.html',{'customer':customer})
@login_required(login_url='customerlogin')
def favourite(request,model,pk):
    customer=request.user.customer
    if model=="House_maintan":
        itm=models.House_maintan.objects.get(id=pk)
        models.Favourite.objects.get_or_create(customer=customer,house_maintan=itm)
        return redirect('house-maintan')
    elif model=="House_sales":
        itm=models.House_sales.objects.get(id=pk)
        models.Favourite.objects.get_or_create(customer=customer,house_sales=itm)
        return redirect('housesales')
    elif model=="land_sales":
        itm=models.land_sales.objects.get(id=pk)
        models.Favourite.objects.get_or_create(customer=customer,land_sales=itm)
        return redirect('landsaleslist')
    
def favourite_page(request):
    if is_customer(request.user):
        fav= models.Favourite.objects.filter(customer=request.user.customer)
        return render(request,"favpage.html",{"fav":fav})
        
    else:
        HttpResponse("You are not a customer")
def removefav(request,id):
    itm=models.Favourite.objects.get(id=id)
    itm.delete()
    return redirect('favpage')

    
def checkstatus(request):
    customer=request.user.customer
    itms=models.customer_orders.objects.filter(customer=customer)
    return render(request,'checkstatus.html',{'itms':itms})
def removeorder(request,id):
    itm=models.customer_orders.objects.get(id=id)
    itm.delete()
    return redirect('checkstatus')