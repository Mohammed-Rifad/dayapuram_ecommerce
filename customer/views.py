from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request,'customer_template/customerhome.html')
def change_password(request):
    return render(request,'customer_template/change_password.html')
def my_order(request):
    return render(request,'customer_template/my_order.html')
def product_details(request):
    return render(request,'customer_template/product_details.html') 
def profile(request):
    return render(request,'customer_template/profile.html')  
def view_cart(request):
    return render(request,'customer_template/view_cart.html') 
def master(request):
    return render(request,'customer_template/master.html') 

def details(request):
    return render(request,'customer_template/details.html') 
