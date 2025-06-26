from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User
from AdminPages.models import Admin
from TeacherPages.models import Teacher

# Create your views here.

def Welcome(request):
    return render(request, 'WebPages/Welcome.html')

def WhyTASKTRAX(request):
    return render(request, 'Webpages/WhyTASKTRAX.html')

def AboutUS(request):
    return render(request, 'Webpages/AboutUs.html')

def ContactUs(request):
    return render(request, 'Webpages/ContactUs.html')

def SignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        isAdmin=(request.POST.get('check') == 'A')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")

        elif password != confirmPassword:
            messages.error(request, "Passwords don't match")

        else:
            myUser = User(username=username, email=email, password=password, isAdmin=isAdmin)
            myUser.save()
            if (isAdmin == True):
                myAdmin = Admin(username=username, email=email, password=password)
                request.session['currentAdmin'] = myAdmin.username
                myAdmin.save()
                return redirect('AdminHome')
            
            else:
                myTeacher = Teacher(username=username, email=email, password=password)
                request.session['currentTeacher'] = myTeacher.username
                myTeacher.save()                
                return redirect('TeacherHome')
                   
    return render(request, 'Webpages/SignUp.html')


def LogIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username = username, password = password).exists():
            if Teacher.objects.filter(username = username, password = password).exists():
                request.session['currentTeacher'] = username
                return redirect('TeacherHome')
            else:
                request.session['currentAdmin'] = username
                return redirect('AdminHome')
            
        else:
            messages.error(request, "Wrong username or password")

    return render(request, "WebPages/LogIn.html")

def AdminHome(request):
    return render(request, "AdminPages/AdminHome.html", {'name':request.session['currentAdmin']})

def TeacherHome(request):
    return render(request, "TeacherPages/TeacherHome.html", {'name':request.session['currentTeacher']})
