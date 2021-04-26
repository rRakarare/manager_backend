from rest_framework import viewsets
from .serializers import ClientSerializer, ProjectSerializer
from projects.models import Client, Project

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()