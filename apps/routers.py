from django.urls import path, include

urlpatterns = [
    path('', include('apps.tasks.urls')),
    path('', include('apps.projects.urls'))
]
