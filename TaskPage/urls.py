from django.urls import path
from . import views

urlpatterns = [
    path('ViewTaskDetails/<int:taskId>', views.ViewTaskDetails, name='ViewTaskDetails'),
]
