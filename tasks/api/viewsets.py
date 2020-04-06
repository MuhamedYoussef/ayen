from tasks.models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        if Task.objects.get(id=kwargs['pk']).state == 'done':
            return super()
        return super().update(request)
