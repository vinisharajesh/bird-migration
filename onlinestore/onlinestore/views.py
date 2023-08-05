from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from onlinestore.form import CreateUserForm
from django.core.mail import send_mail
from.form import ContactForm




def home(request):
    return render(request, 'index.html')



def register(request):
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'password Verified Successfully......!!!')
            return redirect('login')
        else:
            messages.warning(request,'password mismatching......!!!')
            return redirect('register')
    else:
        form=CreateUserForm()
        return render(request, 'register.html',{'form':form})
    
def birddetails(request):
    return render(request,"birddetails.html")
def keerthi(request):

    return render(request,"keerthi.html")
def dailyspeed(request):
    return render(request,"dailyspeed.html")
def dateandtime(request):
    return render(request,"dateandtime.html")
def speed(request):
    return render(request,"speed.html")
def lattitude(request):
    return render(request,"lattitude.html")
def cartographic(request):
    return render(request,"cartographic.html")
