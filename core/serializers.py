from rest_framework import serializers

from core.models import Todo, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
        )


class TodoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Todo
        fields = (
            'id',
            'title',
            'is_completed',
            'created_at',
            'updated_at',
            'tags',
        )


class TodoManageSerializer(TodoSerializer):
    tags = serializers.ListField(child=serializers.CharField(max_length=50))

    def create(self, validated_data):
        title = validated_data['title']
        tags = validated_data['tags']

        todo = Todo.objects.create(title=title)

        for tag in tags:
            todo.add_tag(tag)

        return todo
