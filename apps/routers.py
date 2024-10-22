from django.urls import path, include

urlpatterns = [
    path('tasks/', include('apps.tasks.urls')),
    path('', include('apps.projects.urls'))
]
