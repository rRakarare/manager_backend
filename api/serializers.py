from rest_framework import serializers
from projects.models import Client, Project, Status, Invoice

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields= ['id', 'name', 'image']

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model= Status
        fields= ['id', 'name', 'icontext','subtext', 'order']


class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    class Meta:
        model= Project
        fields= ['id', 'title', 'project_number', 'client', 'status', 'created_at']

class AddProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields= ['id', 'title', 'project_number', 'client', 'status', 'place', 'created_by']

class ProjectSerializerPut(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model= Project
        fields= ['id', 'title', 'client', 'status', 'created_at']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'