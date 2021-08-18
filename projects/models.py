from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext_lazy as _

def upload_to_client(instance, filename):
    return 'clients/{filename}'.format(filename=filename)

def upload_to_crew(instance, filename):
    return 'crew/{filename}'.format(filename=filename)

def upload_to_template(instance, filename):
    return 'template/{filename}'.format(filename=filename)


class WordTemplates(models.Model):
    name=models.CharField(max_length=128, unique=True)
    code=models.CharField(max_length=128, unique=True, blank=True)
    template=models.FileField(upload_to=upload_to_template)

    def __str__(self):
        return str(self.name)

class Crew(models.Model):
    name=models.CharField(max_length=128, unique=True)
    mail=models.EmailField(max_length=128, unique=True)
    role=models.CharField(max_length=128, default="Consultant")
    short=models.CharField(max_length=3, unique=True)
    mobile=models.CharField(max_length=30, unique=True)
    order = models.IntegerField(default=1)
    image = models.ImageField(
        _("Image"), upload_to=upload_to_crew, default='crew/default.png')

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["order"]

class Skill(models.Model):
    text=models.CharField(max_length=256)
    crew = models.ForeignKey(Crew, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ["crew"]


class Artikel(models.Model):
    nominativ = models.CharField(max_length=3, unique=True)
    genitiv = models.CharField(max_length=3)
    dativ = models.CharField(max_length=3)
    akkusativ = models.CharField(max_length=3)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return str(self.nominativ)
    

class Client(models.Model):
    name = models.CharField(max_length=128, unique=True)
    short = models.CharField(max_length=5, default="A")
    artikel = models.ForeignKey(Artikel, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(
        _("Image"), upload_to=upload_to_client, default='clients/default.png')

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
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    project_number = models.CharField(unique=True, max_length=128)
    project_type = models.ForeignKey(ProjectType, null=True, on_delete=models.SET_NULL)
    place = models.CharField(max_length=128, null=True)
    street = models.CharField(max_length=128, null=True)
    plz = models.CharField(max_length=128, null=True)
    contact = models.CharField(max_length=128, null=True)
    part = models.CharField(max_length=128, null=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def update_model(self):
        number = datetime.date.today().strftime("%y") + "-" + self.project_type.short + "-"+ self.client.short + "-" + str(6000+self.id)
        Project.objects.filter(id=self.id).update(project_number=number)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_model()

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
    date_of_payment = models.DateField(null=True, blank=True)
    date_of_invoicing = models.DateField(null=True, blank=True)
    status = models.ForeignKey(InvoiceStatus, null=True, on_delete=models.SET_NULL)

    def update_model(self):
        number = "RN" + "-" + datetime.date.today().strftime("%y") + "-" + str(6000+self.id)
        Invoice.objects.filter(id=self.id).update(invoice_number=number)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_model()

    def __str__(self):
        return str(self.title)

