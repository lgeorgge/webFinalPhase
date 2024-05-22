from django.urls import path
from . import views

urlpatterns = [
    path('AddTask', views.AddTask, name='AddTask'),
    path('EditTask', views.EditTask, name='EditTask'),
    path('ViewAdminTasks', views.ViewAdminTasks, name='ViewAdminTasks'),
]
