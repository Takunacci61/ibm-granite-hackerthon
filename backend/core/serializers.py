from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Only read, automatically set to the logged-in user

    class Meta:
        model = Project
        fields = '__all__'  # Includes all fields
