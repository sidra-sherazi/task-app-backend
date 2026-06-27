from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


# GET all tasks + CREATE task
class TaskListCreateView(generics.ListCreateAPIView):

    queryset = Task.objects.all()

    serializer_class = TaskSerializer


# GET one task + UPDATE + DELETE
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()

    serializer_class = TaskSerializer