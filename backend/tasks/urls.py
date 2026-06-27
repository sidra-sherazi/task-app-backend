from django.urls import path
from .views import TaskListCreateView, TaskDetailView


from django.http import HttpResponse


def home(request):
    return HttpResponse("Backend is running")


urlpatterns = [
    path("", home),
]

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