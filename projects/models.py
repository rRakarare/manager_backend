from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=128, unique=True)

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

class Project(models.Model):
    title = models.CharField(max_length=128)
    project_number = models.CharField(max_length=128, default="none")
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title + " - " + self.client.name)

class Invoice(models.Model):
    title = models.CharField(max_length=256)
    invoice_number = models.CharField(max_length=128)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sent = models.BooleanField(default=False)
    got = models.BooleanField(default=False)

