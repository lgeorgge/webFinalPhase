from django.urls import path
from . import views

urlpatterns = [
    path('AddTask', views.AddTask, name='AddTask'),
    path('EditTask/<int:task_id>/', views.EditTask, name='EditTask'),
    path('ViewAdminTasks', views.ViewAdminTasks, name='ViewAdminTasks'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task')
]
