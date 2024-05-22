from django.shortcuts import render
from TaskPage.models import Task

# Create your views here.

def AddTask(request):
    return render(request, 'AdminPages/AddTask.html')

def EditTask(request):
    return render(request, 'AdminPages/EditTask.html')

def ViewAdminTasks(request):
    return render(request, 'AdminPages/ViewAdminTasks.html', {'tasks':Task.objects.all()})
