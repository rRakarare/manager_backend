from django.contrib import admin
from .djangocsv import ExportCsvMixin
from .models import *

admin.site.register(Client)


@admin.register(Project)
class ProjektAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'getAmount')
    search_fields = ("title__startswith", )

    def getAmount(self, obj):
        invoices = Invoice.objects.filter(project=obj)
        summe = 0
        for invoice in invoices:
            summe = summe + invoice.amount
        return summe

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions = ["export_as_csv"]    



admin.site.register(InvoiceStatus)
admin.site.register(Invoice)

