from django.shortcuts import render

# Create your views here.

def ViewTaskDetails(request):
    return render(request, 'TaskPage/ViewTaskDetails.html')
