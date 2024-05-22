from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import User
from AdminPages.models import Admin
from TeacherPages.models import Teacher
from django.contrib.auth import authenticate, login

# Create your views here.

def Welcome(request):
    return render(request, 'WebPages/Welcome.html')

def WhyTASKTRAX(request):
    return render(request, 'Webpages/WhyTASKTRAX.html')

def AboutUS(request):
    return render(request, 'Webpages/AboutUs.html')

def ContactUs(request):
    return render(request, 'Webpages/ContactUs.html')

currentTeacher = Teacher()
currentAdmin= Admin()

def SignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        isadmin=request.POST.get('check')
        print(isadmin)

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")

        elif password != confirmPassword :
            messages.error(request, "Passwords don't match")

        else:
            myuser = User(username=username, email=email, password=password, isAdmin=isadmin)
            myuser.save()
            if (isadmin == 'A'):
                myadmin = Admin(username=username, email=email, password=password)
                global currentAdmin 
                currentAdmin = Admin(username=username, email=email, password=password)
                myadmin.save()
                return redirect('AdminHome')
            else:
                myteacher = Teacher(username=username, email=email, password=password)
                global currentTeacher 
                currentTeacher = Teacher(username=username, email=email, password=password)
                myteacher.save()
                return redirect('TeacherHome')

            return redirect('LogIn')

    return render(request, 'Webpages/SignUp.html')


def LogIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username = username, password = password).exists():
            if Teacher.objects.filter(username = username, password = password).exists():
                global currentTeacher
                currentTeacher= Teacher.objects.get(username=username)
                print(currentTeacher.username)
                return redirect('TeacherHome')
            else:
                global currentAdmin
                currentAdmin= Admin.objects.get(username=username)
                return redirect('AdminHome')
        else:
            messages.error(request, "Wrong username or password")

    return render(request, "WebPages/LogIn.html")

def TeacherHome(request):
    return render(request, "TeacherPages/TeacherHome.html", {'name':currentTeacher.username})

def AdminHome(request):
    return render(request, "AdminPages/AdminHome.html", {'name':currentAdmin.username})
