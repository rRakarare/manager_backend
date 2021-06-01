from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    return 'clients/{filename}'.format(filename=filename)

class Client(models.Model):
    name = models.CharField(max_length=128, unique=True)
    short = models.CharField(max_length=5, default="none")
    image = models.ImageField(
        _("Image"), upload_to=upload_to, default='clients/default.png')

    def __str__(self):
        return str(self.name)

class Status(models.Model):
    name = models.CharField(max_length=128, unique=True)
    order = models.IntegerField(default=1)
    icontext = models.CharField(max_length=128, default="icontext")
    subtext = models.CharField(max_length=128, default="text")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return (str(self.order) + " - "+ self.name)

class ProjectType(models.Model):
    name = models.CharField(max_length=128, unique=True)
    short = models.CharField(max_length=4, unique=True)
    
    def __str__(self):
        return str(self.name)



class Project(models.Model):
    title = models.CharField(max_length=128)
    project_number = models.CharField(unique=True, max_length=128)
    project_type = models.ForeignKey(ProjectType, null=True, on_delete=models.SET_NULL)
    place = models.CharField(max_length=128, null=True)
    street = models.CharField(max_length=128, null=True)
    plz = models.CharField(max_length=128, null=True)
    contact = models.CharField(max_length=128, null=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.project_number = datetime.date.today().strftime("%y") + "-" + self.client.short + self.project_type.short + "-"
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

class InvoiceStatus(models.Model):
    name = models.CharField(max_length=128)
    order = models.IntegerField(default=1)
    icontext = models.CharField(max_length=128, default="icontext")
    
    class Meta:
        ordering = ["order"]

    def __str__(self):
        return (str(self.order) + " - "+ self.name)

class Invoice(models.Model):
    title = models.CharField(max_length=256)
    invoice_number = models.CharField(unique=True, max_length=128)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_payment = models.DateTimeField(null=True, blank=True)
    date_of_invoicing = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(InvoiceStatus, null=True, on_delete=models.SET_NULL)

