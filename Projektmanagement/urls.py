"""
URL configuration for Projektmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from Projektmanagement import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.main_view, name='main'),
    path('projects/', views.project_overview, name='project_overview'),
    path('projects/create', views.project_create, name='project_create'),
    path('projects/create/submission', views.project_create_submission, name="project_create_submission"),
    path('projects/update/<int:id>/', views.project_update, name='project_update'),
    path('projects/delete', views.project_delete, name='project_delete'),
    path('projects/delete/<int:id>/', views.project_delete_new, name='project_delete_new'),
    path('task/<int:task_id>', views.task_update, name='task'),
    path('tasks/<int:project_id>', views.task_overview, name='tasks_overview'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/create/<int:project_id>', views.task_create, name='project_task_create'),
    path('task/delete_page/<int:task_id>', views.task_delete_page, name='task_delete_page'),
    path('task/delete/<int:task_id>', views.task_delete, name='task_delete'),
    path('task/update/<int:task_id>', views.task_update, name='task_update'),
    path('user/<int:id>/', views.user_view, name='user'),
    path('toggle_completed/<int:task_id>/', views.toggle_completed, name='toggle_completed'),
]
