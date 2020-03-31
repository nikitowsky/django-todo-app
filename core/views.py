from rest_framework import viewsets, status
from rest_framework.response import Response

from core.models import Todo, Tag
from core.serializers import TodoSerializer, TodoManageSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def list(self, request):
        todos = self.get_queryset()
        serializer = self.serializer_class(todos, many=True)

        return Response({'data': serializer.data})

    def retrieve(self, request, pk=None):
        todo = self.get_object()
        serializer = self.serializer_class(todo)

        return Response({'data': serializer.data})

    def create(self, request):
        serializer = TodoManageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.create(request.data)

            return Response({'data': serializer.data})
        else:
            return Response({'errors': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        todo = self.get_object()
        serializer = self.serializer_class(todo)
        request_serializer = TodoManageSerializer(data=request.data)

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
            return Response({'errors': request_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        todo = self.get_object()
        serializer = self.serializer_class(todo)
        serialized_data = serializer.data

        todo.delete()

        return Response({'data': serialized_data})
