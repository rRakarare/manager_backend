from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ClientSerializer, AddProjectSerializer, ProjectSerializer, StatusSerializer, ProjectSerializerPut, InvoiceSerializer, ProjectTypeSerializer, ArtikelSerializer, UpdateProjectSerializer, InvoiceStatusSerializer, CrewSerializer, SkillSerializer, TemplateSerializer, InvoiceNumbersSerializer
from projects.models import Client, Project, Status, Invoice, ProjectType, Artikel, InvoiceStatus, Crew, Skill, WordTemplates, InvoiceNumbers


class TemplateViewSet(viewsets.ModelViewSet):
    serializer_class = TemplateSerializer
    queryset = WordTemplates.objects.all()

class InvoiceStatusViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceStatusSerializer
    queryset = InvoiceStatus.objects.all()

class ArtikelViewSet(viewsets.ModelViewSet):
    serializer_class = ArtikelSerializer
    queryset = Artikel.objects.all()

class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    

class ProjectTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectTypeSerializer
    queryset = ProjectType.objects.all()

class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class InvoiceNumberView(viewsets.ModelViewSet):
    serializer_class = InvoiceNumbersSerializer
    queryset = InvoiceNumbers.objects.all()

class AddProject(generics.ListCreateAPIView):
    serializer_class = AddProjectSerializer
    queryset = Project.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        print(request.user)
        data["created_by"] = request.user.id
        serializer = AddProjectSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ProjectPutView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializerPut
    queryset = Project.objects.all()

class ProjectUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UpdateProjectSerializer
    queryset = Project.objects.all()

class InvoiceAll(generics.ListCreateAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

class InvoiceViewSingle(generics.ListCreateAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

    def get_queryset(self):
        project_id = self.request.query_params.get('id')
        queryset = Invoice.objects.filter(project=project_id)
        return queryset

class InvoiceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()

class PostClient(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CrewAll(generics.ListCreateAPIView):
    serializer_class = CrewSerializer
    queryset = Crew.objects.all()

class SkillAll(generics.ListCreateAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()



