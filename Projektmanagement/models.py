from django.db import models
# ToDo: correct following imports
from django.db.models import Manager
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    last_changed = models.DateField(default=start_date)
    notes = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    users = models.ManyToManyField(User, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.name