from django.urls import path
from .views import TaskListCreateView, TaskDetailView


urlpatterns = [

    path(
        'api/tasks/',
        TaskListCreateView.as_view()
    ),


    path(
        'api/tasks/<int:pk>/',
        TaskDetailView.as_view()
    ),

]