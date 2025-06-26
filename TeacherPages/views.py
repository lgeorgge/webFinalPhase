from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from TaskPage.models import Task

# Create your views here.

def ViewTeacherTasks(request):
    currentTeacher = request.session.get('currentTeacher')
    if request.method == 'POST':
        searchQuery = request.POST.get('searchForTeacherTask', '')
        filters = request.POST.getlist('filter')
        querySet = Task.objects.filter(teacherName=currentTeacher)

        if searchQuery:
            querySet = querySet.filter(
                Q(taskID__icontains=searchQuery) |
                Q(title__icontains=searchQuery) |
                Q(teacherName__icontains=searchQuery)
            )

        if filters:
            priorityFilter = Q()
            statusFilter = Q()

            for f in filters:
                if f in ['Low', 'Medium', 'High']:
                    priorityFilter |= Q(priority=f)

                elif f == 'Completed':
                    statusFilter |= Q(status=True)

                elif f == 'Uncompleted':
                    statusFilter |= Q(status=False)

            if priorityFilter:
                querySet = querySet.filter(priorityFilter)

            if statusFilter:
                querySet = querySet.filter(statusFilter)

        context = {'tasks': querySet}

    else:
        context = {'tasks': Task.objects.filter(teacherName=currentTeacher)}

    return render(request, 'TeacherPages/ViewTeacherTasks.html', context)

def ChangeTaskStatus(request, taskId):
    if request.method == 'POST':
        task = Task.objects.get(taskID = taskId)
        task.status =  not task.status
        task.save()
        return JsonResponse({'success':True})
