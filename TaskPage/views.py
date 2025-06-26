from django.shortcuts import render, get_object_or_404
from TaskPage.models import Task

# Create your views here.

def ViewTaskDetails(request, taskId):
    task = get_object_or_404(Task, taskID=taskId)
    return render(request, 'TaskPage/ViewTaskDetails.html', {'task':task})
