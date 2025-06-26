from django.urls import path
from . import views

urlpatterns = [
    path('AddTask', views.AddTask, name='AddTask'),
    path('EditTask/<int:taskId>', views.EditTask, name='EditTask'),
    path('ViewAdminTasks', views.ViewAdminTasks, name='ViewAdminTasks'),
    path('DeleteTask/<int:taskId>', views.DeleteTask, name='DeleteTask')
]
