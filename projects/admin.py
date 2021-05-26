from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

admin.site.register(Client)

class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project
        skip_unchanged = True
        report_skipped = False

class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource
    list_display = ('title', 'client', 'getAmount')
    search_fields = ("title__startswith", )

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



admin.site.register(InvoiceStatus)
admin.site.register(Invoice)

