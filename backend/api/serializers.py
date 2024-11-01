"""Serializers."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Task сериалазйер."""

    class Meta:
        """Класс Мета."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
