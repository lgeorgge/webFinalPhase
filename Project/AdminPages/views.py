from django.contrib import messages
from django.shortcuts import redirect, render
from TaskPage.models import Task
from AdminPages.models import Admin
from TeacherPages.models import Teacher
from WebPages.views import currentAdmin





# taskID = models.IntegerField(default=0)
#     title = models.CharField(max_length=100)
#     teacherName = models.CharField(max_length=100)
#     priority = models.CharField(max_length=10, choices = taskPriority)
#     description = models.TextField(max_length=1000)
#     createdBy = models.CharField(max_length=100)
#     status = models.BooleanField(default=False, choices 
# Create your views here.

def AddTask(request):
    if request.method == 'POST':
        taskId = request.POST['ID']
        taskTitle = request.POST['title']
        teacherName = request.POST['name']
        taskDescription = request.POST['description']
        taskPriorty = request.POST.get('priority')
        global currentAdmin
        name=currentAdmin.username
        if Task.objects.filter(taskID = taskId):
            messages.error(request, "there is already a task with this ID")
        elif Teacher.objects.filter(username = teacherName):
            task = Task(taskID=taskId, 
                        title=taskTitle, 
                        teacherName=teacherName,
                        description=taskDescription, 
                        priority=taskPriorty,createdBy = request.session.get('current_admin_name')
                        )
            if taskPriorty == "low":
                task.priority = "Low"
            elif taskPriorty == "medium":
                task.priority = "Medium"
            else:
                task.priority = "High"
            

            task.save()
            return render(request,'AdminPages/ViewAdminTasks.html')
        else : 
            messages.error(request, "there is no teacher with this name")
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
