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
