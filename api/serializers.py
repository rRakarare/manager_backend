from rest_framework import serializers
from projects.models import Client, Project, Status, Invoice, ProjectType, Artikel, InvoiceStatus, Crew, Skill, WordTemplates, InvoiceNumbers

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model= WordTemplates
        fields= ['id', 'name', 'code', 'template']

class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model= Crew
        fields= ['id', 'name', 'image', 'role', 'short', 'mobile', 'mail']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model= Skill
        fields= ['id', 'text', 'crew']

class InvoiceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model= InvoiceStatus
        fields= ['id', 'name', 'order', 'icontext']

class ArtikelSerializer(serializers.ModelSerializer):
    class Meta:
        model= Artikel
        fields= ['id', 'nominativ', 'genitiv', 'dativ', 'akkusativ']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields= ['id', 'name', 'short', 'artikel', 'image']
        extra_kwargs = {'artikel' : {'required':True}, 'short' : {'required':True}}

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model= Status
        fields= ['id', 'name', 'icontext','subtext', 'order']

class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProjectType
        fields= ['id', 'name', 'short']

class InvoiceNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model= InvoiceNumbers
        fields= ['id', 'short', 'year', 'number']


class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    class Meta:
        model= Project
        fields= ['id', 'title', 'project_type', 'project_number', 'client', 'status', 'created_at']

class AddProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields= ['id', 'title', 'project_type', 'client', 'status', 'place', 'created_by']
        extra_kwargs = {
            'client': {'required': True},
            'project_type': {'required': True},
            } 

class ProjectSerializerPut(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model= Project
        fields= ['id', 'title', 'project_number', 'client', 'status', 'created_at', 'place', 'part', 'plz', 'street', 'contact']

class UpdateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields= ['id', 'title', 'client', 'status', 'created_at', 'place', 'part', 'plz', 'street', 'contact']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'title', 'invoice_number', 'amount', 'date_of_invoicing', 'project', 'status', 'date_of_payment']
        extra_kwargs = {
            'invoice_number': {'required': False},
            'date_of_payment': {'required': True},
            } 