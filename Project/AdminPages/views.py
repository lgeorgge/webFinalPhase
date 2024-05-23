from django.contrib import messages
from django.shortcuts import redirect, render
from TaskPage.models import Task
from AdminPages.models import Admin
from TeacherPages.models import Teacher
from WebPages.views import currentAdmin
from django.shortcuts import get_object_or_404




def AddTask(request):
    if request.method == 'POST':
        taskId = request.POST['ID']
        taskTitle = request.POST['title']
        teacherName = request.POST['name']
        taskDescription = request.POST['description']
        taskPriority = request.POST.get('priority')

        if Task.objects.filter(taskID=taskId).exists():
            messages.error(request, "There is already a task with this ID")
        elif Teacher.objects.filter(username=teacherName).exists():
            task = Task(
                taskID=taskId,
                title=taskTitle,
                teacherName=teacherName,
                description=taskDescription,
                priority=taskPriority,
                createdBy=request.session.get('current_admin_name')
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


def ViewAdminTasks(request):
    return render(request, 'AdminPages/ViewAdminTasks.html', {'tasks':Task.objects.all()})

def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, taskID=task_id)
        task.delete()
        #messages.success(request, "Task deleted successfully")
        return redirect('ViewAdminTasks')
    else:
        messages.error(request, "Invalid request method for task deletion")
        return redirect('ViewAdminTasks')
    
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from TaskPage.models import Task
from TeacherPages.models import Teacher

def EditTask(request, task_id):
    task = get_object_or_404(Task, taskID=task_id)
    
    if request.method == 'POST':
        taskTitle = request.POST.get('title')
        teacherName = request.POST.get('name')
        taskDescription = request.POST.get('description')
        taskPriority = request.POST.get('priority')

        if not taskTitle or not teacherName or not taskDescription or not taskPriority:
            messages.error(request, "All fields are required.")
        elif not Teacher.objects.filter(username=teacherName).exists():
            messages.error(request, "There is no teacher with this name")
        else:
            task.title = taskTitle
            task.teacherName = teacherName
            task.description = taskDescription
            task.priority = taskPriority.capitalize()

            task.save()
            messages.success(request, "Task updated successfully")
            return redirect('ViewAdminTasks')
    
    return render(request, 'AdminPages/EditTask.html', {'task': task})



