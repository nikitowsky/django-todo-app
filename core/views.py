from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from core.models import Todo
from core.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    renderer_classes = (JSONRenderer, )

    def list(self, request, *args, **kwargs):
        todos = self.get_queryset()
        serializer = self.get_serializer(todos, many=True)

        return Response({'data': serializer.data})
