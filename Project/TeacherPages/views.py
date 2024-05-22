from django.shortcuts import render
from django.db.models import Q
from TaskPage.models import Task

# Create your views here.

def ViewTeacherTasks(request):
    if request.method == 'POST':
        search_query = request.POST.get('searchForTeacherTask', '')
        filters = request.POST.getlist('filter')

        queryset = Task.objects.all()

        if search_query:
            queryset = queryset.filter(
                Q(taskID__icontains=search_query) |
                Q(title__icontains=search_query) |
                Q(teacherName__icontains=search_query)
            )

        if filters:
            priority_filters = Q()
            status_filters = Q()
            for f in filters:
                if f in ['Low', 'Medium', 'High']:
                    priority_filters |= Q(taskPriority=f)
                elif f == 'Completed':
                    status_filters |= Q(taskStatus=True)
                elif f == 'Uncompleted':
                    status_filters |= Q(taskStatus=False)

            if priority_filters:
                queryset = queryset.filter(priority_filters)
            if status_filters:
                queryset = queryset.filter(status_filters)

        context = {'tasks': queryset}
    else:
        context = {'tasks': Task.objects.all()}

    return render(request, 'TeacherPages/ViewTeacherTasks.html', context)
