from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def signupPage(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        eml=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('confirmpassword')
        #print(uname,eml,pass1)
        
        my_user=User.objects.create_user(uname,eml,pass1)
        my_user.save()
        return redirect('login')
        #return HttpResponse("user created successfully!")
    return render(request,'signup.html')

def loginPage(request):
    if request.method=="POST":
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        user=authenticate(request,username=username1,password=password1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid username or password!")
    return render(request,'login.html')

def homePage(request):
    return render(request,'home.html')

def logoutPage(request):
    logout(request)
    return redirect('login')
# Create your views here.
