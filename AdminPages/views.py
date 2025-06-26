from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from TaskPage.models import Task
from TeacherPages.models import Teacher

# Create your views here.

def ViewAdminTasks(request):
    currentAdmin = request.session.get('currentAdmin')
    if request.method == 'POST':
        searchQuery = request.POST.get('searchForAdminTask', '')
        querySet = Task.objects.filter(createdBy=currentAdmin)

        if searchQuery:
            querySet = querySet.filter(
                Q(taskID__icontains=searchQuery) |
                Q(title__icontains=searchQuery) |
                Q(teacherName__icontains=searchQuery)
            )

        context = {'tasks': querySet}

    else:
        context = {'tasks': Task.objects.filter(createdBy=currentAdmin)}

    return render(request, 'AdminPages/ViewAdminTasks.html', context)

def AddTask(request):
    if request.method == 'POST':
        taskID = request.POST['ID']
        taskTitle = request.POST['title']
        teacherName = request.POST['name']
        taskDescription = request.POST['description']
        taskPriority = request.POST.get('priority')

        if Task.objects.filter(taskID=taskID).exists():
            messages.error(request, "Task ID already taken")

        elif Teacher.objects.filter(username=teacherName).exists():
            task = Task(
                taskID=taskID,
                title=taskTitle,
                teacherName=teacherName,
                description=taskDescription,
                priority=taskPriority,
                createdBy=request.session.get('currentAdmin')
            )

            if taskPriority == "low":
                task.priority = "Low"

            elif taskPriority == "medium":
                task.priority = "Medium"

            else:
                task.priority = "High"

            task.save()
            return redirect('ViewAdminTasks')
        
        else:
            messages.error(request, "There is no teacher with this name")

    return render(request, 'AdminPages/AddTask.html')


def EditTask(request, taskId):
    task = get_object_or_404(Task, taskID=taskId)
    
    if request.method == 'POST':
        taskTitle = request.POST.get('title')
        teacherName = request.POST.get('name')
        taskDescription = request.POST.get('description')
        taskPriority = request.POST.get('priority')

        if not Teacher.objects.filter(username=teacherName).exists():
            messages.error(request, "There is no teacher with this name")

        else:
            task.title = taskTitle
            task.teacherName = teacherName
            task.description = taskDescription
            task.priority = taskPriority.capitalize()
            task.save()
            return redirect('ViewAdminTasks')
    
    return render(request, 'AdminPages/EditTask.html', {'task':task})

def DeleteTask(request, taskId):
    if request.method == 'POST':
        task = get_object_or_404(Task, taskID=taskId)
        task.delete()
        return JsonResponse({'success':True})
