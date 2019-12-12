from rest_framework import serializers

from core.models import Todo, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        read_only_fields = ('basemodel_ptr', )
        fields = (
            'id',
            'title',
        )


class TodoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Todo
        read_only_fields = ('basemodel_ptr', )
        fields = (
            'id',
            'title',
            'is_completed',
            'created_at',
            'updated_at',
            'tags',
        )
