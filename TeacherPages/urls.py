from django.urls import path
from . import views

urlpatterns = [
    path('ViewTeacherTasks', views.ViewTeacherTasks, name='ViewTeacherTasks'),
    path('ChangeTaskStatus/<int:taskId>', views.ChangeTaskStatus, name='ChangeTaskStatus'),
]
