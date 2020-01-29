from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from core.models import Todo, Tag
from core.serializers import (
    TodoSerializer,
    TodoUpdateSerializer,
    TodoCreateSerializer,
)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    renderer_classes = (JSONRenderer, )

    def list(self, request):
        todos = self.get_queryset()
        serializer = TodoSerializer(todos, many=True)
        serialized_data = serializer.data

        return Response({'data': serialized_data})

    def create(self, request):
        title = request.data.get('title')
        tags = request.data.get('tags')
        request_serializer = TodoCreateSerializer(data=request.data)

        if request_serializer.is_valid():
            todo = Todo.objects.create(title=title)

            for tag in tags:
                tag, created = Tag.objects.get_or_create(title=tag)

                if not created:
                    tag = Tag.objects.get(title=tag)

                todo.tags.add(tag)

            serializer = self.get_serializer(todo)

            return Response({'data': serializer.data})
        else:
            return Response({'errors': request_serializer.errors})

    def partial_update(self, request, pk=None):
        todo = self.get_object()
        serializer = TodoSerializer(todo)
        request_serializer = TodoUpdateSerializer(data=request.data)

        if request_serializer.is_valid():
            title = request.data.get('title')
            tags = request.data.get('tags')

            todo.title = title
            todo.tags.clear()

            for tag in tags:
                tag, created = Tag.objects.get_or_create(title=tag)

                if not created:
                    tag = Tag.objects.get(title=tag)

                todo.tags.add(tag)

            todo.save()

            return Response({'data': serializer.data})
        else:
            return Response({'errors': request_serializer.errors})

    def retrieve(self, request, pk=None):
        todo = self.get_object()
        serializer = TodoSerializer(todo)
        serialized_data = serializer.data

        return Response({'data': serialized_data})

    def destroy(self, request, pk=None):
        todo = self.get_object()
        serializer = TodoSerializer(todo)
        serialized_data = serializer.data

        todo.delete()

        return Response({'data': serialized_data})
