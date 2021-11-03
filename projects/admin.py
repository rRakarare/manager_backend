from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class SkillResource(resources.ModelResource):
    class Meta:
        model = Skill
        skip_unchanged = True
        report_skipped = False

class SkillAdmin(ImportExportModelAdmin):
    resource_class = SkillResource
    list_display = ('text', 'crew')

admin.site.register(Skill, SkillAdmin)

class CrewResource(resources.ModelResource):
    class Meta:
        model = Crew
        skip_unchanged = True
        report_skipped = False

class CrewAdmin(ImportExportModelAdmin):
    resource_class = CrewResource
    list_display = ('name', 'short')

admin.site.register(Crew, CrewAdmin)


class ArtikelResource(resources.ModelResource):
    class Meta:
        model = Artikel
        skip_unchanged = True
        report_skipped = False

class ArtikelAdmin(ImportExportModelAdmin):
    resource_class = ArtikelResource
    list_display = ('nominativ', 'order')

admin.site.register(Artikel, ArtikelAdmin)


class ClientResource(resources.ModelResource):
    class Meta:
        model = Client
        skip_unchanged = True
        report_skipped = False

class ClientAdmin(ImportExportModelAdmin):
    resource_class = ClientResource
    list_display = ('name', 'image')

admin.site.register(Client, ClientAdmin)

class ProjectTypeResource(resources.ModelResource):
    class Meta:
        model = ProjectType
        skip_unchanged = True
        report_skipped = False

class ProjectTypeAdmin(ImportExportModelAdmin):
    resource_class = ProjectTypeResource
    list_display = ('name', 'short')


admin.site.register(ProjectType, ProjectTypeAdmin)

class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project
        skip_unchanged = True
        report_skipped = False

class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource
    list_display = ('title', 'client', 'getAmount')
    search_fields = ("title__startswith", )
    exclude = ('is_created',)

    def getAmount(self, obj):
        invoices = Invoice.objects.filter(project=obj)
        summe = 0
        for invoice in invoices:
            summe = summe + invoice.amount
        return summe

admin.site.register(Project, ProjectAdmin)


class StatusResource(resources.ModelResource):
    class Meta:
        model = Status
        skip_unchanged = True
        report_skipped = False

class StatusAdmin(ImportExportModelAdmin):
    resource_class = StatusResource
    list_display = ('name', 'order')


admin.site.register(Status, StatusAdmin)

class InvoiceStatusResource(resources.ModelResource):
    class Meta:
        model = InvoiceStatus
        skip_unchanged = True
        report_skipped = False

class InvoiceStatusAdmin(ImportExportModelAdmin):
    resource_class = InvoiceStatusResource
    list_display = ('name', 'order')



admin.site.register(InvoiceStatus, InvoiceStatusAdmin)


class InvoiceResource(resources.ModelResource):
    class Meta:
        model = Invoice
        skip_unchanged = True
        report_skipped = False

class InvoiceAdmin(ImportExportModelAdmin):
    resource_class = InvoiceResource
    list_display = ('invoice_number', 'title', 'amount')

admin.site.register(Invoice, InvoiceAdmin)

admin.site.register(WordTemplates)
admin.site.register(InvoiceNumbers)
