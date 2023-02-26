"""Office_emp_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name= "index" ),
    path('add_emp', views.add_emp, name= "Add Employee" ),
    path('view_all_emp', views.view_all_emp, name= "View All Employee" ),
    path('filter_emp', views.filter_emp, name= "Filter employee" ),
    path('remove_emp', views.remove_emp, name= "Remove Employee" ),
    path('remove_emp/<int:emp_id>', views.remove_emp, name= "Remove Employee" ),
]
