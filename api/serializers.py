from rest_framework import serializers
from projects.models import Client, Project

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields= ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields= ['id', 'title', 'client']
