from django.db import models
# ToDo: correct following imports
from django.db.models import Manager
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    last_changed = models.DateField()
    notes = models.TextField()
    owner = models.ForeignKey(Manager, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    done = models.BooleanField(default=False)
    description = models.TextField()
    users = models.ManyToManyField(User)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.name