from django.contrib import admin
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


admin.site.register(Status)


admin.site.register(Invoice)

