from django.urls import path, include
from .views.project_views import ProjectsApi

urlpatterns = [
    path('projects/',ProjectsApi.as_view()),

]