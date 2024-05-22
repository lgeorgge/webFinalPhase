from django.shortcuts import render
from TaskPage.models import Task
from AdminPages.models import Admin
from TeacherPages.models import Teacher

# Create your views here.

def AddTask(request):
    if request.method == 'POST':
        taskId = request.Post['ID']
        taskTitle = request.Post['title']
        teacherName = request.Post['name']
        taskDescription = request.Post['description']

        
        

    return render(request, 'AdminPages/AddTask.html')

def EditTask(request):
    return render(request, 'AdminPages/EditTask.html')

def ViewAdminTasks(request):
    return render(request, 'AdminPages/ViewAdminTasks.html', {'tasks':Task.objects.all()})



# def SignUp(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirmPassword = request.POST['confirmPassword']
#         isadmin=request.POST.get('check')
#         print(isadmin)

#         if User.objects.filter(username=username):
#             messages.error(request, "Username already exists")

#         elif password != confirmPassword :
#             messages.error(request, "Passwords don't match")

#         else:
#             myuser = User(username=username, email=email, password=password, isAdmin=isadmin)
#             myuser.save()
#             if (isadmin == 'A'):
#                 myadmin = Admin(username=username, email=email, password=password)
#                 global currentAdmin 
#                 currentAdmin = Admin(username=username, email=email, password=password)
#                 myadmin.save()
#                 return redirect('AdminHome')
#             else:
#                 myteacher = Teacher(username=username, email=email, password=password)
#                 global currentTeacher 
#                 currentTeacher = Teacher(username=username, email=email, password=password)
#                 myteacher.save()
#                 return redirect('TeacherHome')

#             return redirect('LogIn')

#     return render(request, 'Webpages/SignUp.html')

# def LogIn(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         if User.objects.filter(username = username, password = password).exists():
#             if Teacher.objects.filter(username = username, password = password).exists():
#                 global currentTeacher
#                 currentTeacher= Teacher.objects.get(username=username)
#                 print(currentTeacher.username)
#                 return redirect('TeacherHome')
#             else:
#                 global currentAdmin
#                 currentAdmin= Admin.objects.get(username=username)
#                 return redirect('AdminHome')
#         else:
#             messages.error(request, "Wrong username or password")

#     return render(request, "WebPages/LogIn.html")
