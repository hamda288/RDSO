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

        if len(pass1)<8:
           return HttpResponse("password must be of atleast 8 characters")
        if(pass1.isalnum()==pass1 or pass1.upper()==pass1 or pass1.lower()==pass1):
            return HttpResponse("pass must have atleast 1 uppercase character, 1 digit and 1 lowercase character!")
        elif(pass1.isalnum()==pass1 and pass1.upper()==pass1 and pass1.lower()==pass1):
            return HttpResponse("pass must have atleast 1 uppercase character, 1 digit and 1 lowercase character!")
        elif(pass1.isalnum()==pass1 and pass1.upper()==pass1 and pass1.lower()==pass1):
            return HttpResponse("pass must have atleast 1 uppercase character, 1 digit and 1 lowercase character!")
        else:
            if pass1==pass2:
                if User.objects.filter(username=uname).exists():
                    return HttpResponse("Username already taken!")
                elif User.objects.filter(email=eml).exists():
                    return HttpResponse("Email already taken!")
                else:
                    my_user=User.objects.create_user(uname,eml,pass1)
                    my_user.save()
            else:
                return HttpResponse("Password not matching!")
        return redirect('login')
        #return HttpResponse("user created successfully!")
    return render(request,'signup.html')

def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
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
