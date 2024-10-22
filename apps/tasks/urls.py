from django.urls import path

from apps.tasks.views.tag_views import *
from apps.tasks.views.task_views import *

urlpatterns = [
    path('tag/', TagListApi.as_view(), name='tag'),
    path('tag/<int:pk>/', TagApi.as_view(), name='tag'),
    path('tasks/', TasksListAPIView.as_view(), name='tasks'),
]
