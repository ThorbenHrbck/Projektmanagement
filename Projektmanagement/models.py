from datetime import date, timedelta
from django.db import models

#----------------------------------------------------------------------------------------------------------

class User(models.Model):
    firstName = models.CharField(max_length=50, null=True)    # mögliche länge der eingaben sollte bei allen Gleich sein, maybe auf 255 setzen
    lastName = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=50)
    workhours = models.IntegerField(null=True)
    def __str__(self):
        return self.firstName + ' ' + self.lastName

#----------------------------------------------------------------------------------------------------------

class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    last_changed = models.DateField(default=start_date, null=True, blank=True)    # könnte raus genommen werden, hällt, finde ich, keine relevanten Informationen
    notes = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    users = models.ManyToManyField(User, null=True, blank=True)    # welcher User ist hier gemeint, der erstellt oder der zugewiesen wird? Namensgebung ändern
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#----------------------------------------------------------------------------------------------------------
class Sprint(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(null=False, blank=True)
    end_date = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)
    hours = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # 'done' is true when end_date in the past
        if self.end_date and self.end_date < date.today():
         self.done = True
        else:
            self.done = False

        self.hours = self.workhours()
        super().save(*args, **kwargs)

    def __str__(self):
     return self.name

    def workhours(self):
        # No workdays between start_date und end_date.
        if not self.start_date or not self.end_date:
            return 0

        workdays = 0
        current_date = self.start_date
        while current_date <= self.end_date:
            if current_date.weekday() < 5:  # Monday=0, Sunday=6
                workdays += 1
            current_date += timedelta(days=1)
        return workdays * 8 # 8-Hour Days
