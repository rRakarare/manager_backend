from rest_framework import viewsets
from .serializers import ClientSerializer, ProjectSerializer, StatusSerializer
from projects.models import Client, Project, Status

class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()