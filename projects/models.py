from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return str(self.name)

class Status(models.Model):
    name = models.CharField(max_length=128, unique=True)
    def __str__(self):
        return str(self.name)

class Project(models.Model):
    title = models.CharField(max_length=128)
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title + " - " + self.client.name)

