from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome, name='Welcome'),
    path('WhyTASKTRAX', views.WhyTASKTRAX, name='WhyTASKTRAX'),
    path('AboutUs', views.AboutUS, name='AboutUs'),
    path('ContactUs', views.ContactUs, name='ContactUs'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('LogIn', views.LogIn, name='LogIn'),
    path('AdminHome', views.AdminHome, name='AdminHome'),
    path('TeacherHome', views.TeacherHome, name='TeacherHome'),
]
