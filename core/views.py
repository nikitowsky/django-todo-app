from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from core.models import Todo, Tag
from core.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    renderer_classes = (JSONRenderer, )

    def list(self, request):
        todos = self.get_queryset()
        serializer = self.get_serializer(todos, many=True)

        return Response({'data': serializer.data})

    def create(self, request):
        title = request.data.get('title')
        tags = request.data.get('tags')

        todo = Todo.objects.create(title=title)

        for tag in tags:
            tag, created = Tag.objects.get_or_create(title=tag)

            if not created:
                tag = Tag.objects.get(title=tag)

            todo.tags.add(tag)

        serializer = self.get_serializer(todo)

        return Response({'data': serializer.data})

    def destroy(self, request, pk=None):
        try:
            todo = Todo.objects.get(id=pk)

            todo.delete()
            serializer = self.get_serializer(todo)

            return Response({'data': serializer.data})
        except Todo.DoesNotExist:
            return Response({'message': 'Not found'}, status=404)
