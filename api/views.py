from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serializers import ClientSerializer, ProjectSerializer, StatusSerializer, ProjectSerializerPut, InvoiceSerializer
from projects.models import Client, Project, Status, Invoice

class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectPutView(generics.RetrieveUpdateAPIView):
    serializer_class = ProjectSerializerPut
    queryset = Project.objects.all()

class InvoiceViewSingle(generics.ListAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

    def get_queryset(self):
        project_id = self.request.query_params.get('id')
        queryset = Invoice.objects.filter(project=project_id)
        return queryset

