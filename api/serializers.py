from rest_framework import serializers
from projects.models import Client, Project, Status

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields= ['id', 'name']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model= Status
        fields= ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    class Meta:
        model= Project
        fields= ['id', 'title', 'client', 'status', 'created_at']
