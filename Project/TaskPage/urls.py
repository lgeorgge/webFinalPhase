from django.urls import path
from . import views

urlpatterns = [
    path('ViewTaskDetails', views.ViewTaskDetails, name='ViewTaskDetails'),
]
