from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.db import IntegrityError
from app1.models import Employees
# Create your views here.

@never_cache
def AdminPanel(request):
    if not request.user.is_superuser:
        return redirect('login')
    emp = Employees.objects.all()

    context = {
        'emp':emp
    }
    return render(request, 'index.html', context)

@never_cache
def AdminLogin(request):
    if request.user.is_superuser:
        return redirect('panel')
    
    if request.method == 'POST':
         # Extract username and password from POST data
         username = request.POST.get('username')
         password = request.POST.get('password')

         # Authenticate the user
         user = authenticate(request, username = username, password = password)

        # If authentication is successful, log the user in
         if user is not None:
             login(request, user)
             return redirect('panel')
         else:
             error_message = 'Username or Password is incorrect'
             return render(request, 'adminlogin.html', {'error_message': error_message})
             
    return render(request, 'adminlogin.html')

def Add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees (
            name = name,
            email = email, 
            address = address,
            phone = phone
        )
        emp.save()
        return redirect('panel')

    return redirect(request, 'panel')

def Edit(request):
    emp = Employees.objects.all()

    context = {
        'emp' : emp, 
    }
    return redirect(request , 'panel', context)

def Update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id = id,
            name = name, 
            email = email, 
            address = address,
            phone = phone,
        )
        emp.save( )
        return redirect('panel')

    return redirect(request, 'panel')

def Delete(request, id):
    emp = Employees.objects.filter(id = id)
    emp.delete()
    context = {
        'emp': emp,
    }
    return redirect('panel')

def AdminLogout(request):
    if request.user.is_superuser:
        logout(request)
        return redirect('adminlogin')

@never_cache
@login_required(login_url='login')
def HomePage(request):
    return render (request, 'home.html')

@never_cache
def SignupPage(request):    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')


        if pass1 != pass2:
            error_message = 'your passwords are not match'             
            return render(request, 'signup.html', {'error_message': error_message})
        else:
            try:
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                return redirect('login')
            except IntegrityError:
                error_message = 'Username already exists. Please choose a different username.'
                return render(request, 'signup.html', {'error_message': error_message})
       
    
    return render (request, 'signup.html')

@never_cache
def LoginPage(request):
    if request.user.is_authenticated:
        return redirect ('home')
    
    if request.method == 'POST':
        # Extract username and password from POST data
        username = request.POST.get('username')
        pass1 = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username = username, password = pass1)

        # If authentication is successful, log the user in
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse ('Username or password is incorrect')
        
    # Render the login page for GET requests or failed POST requests
    return render (request, 'login.html')

@never_cache
def LogoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('signup')


