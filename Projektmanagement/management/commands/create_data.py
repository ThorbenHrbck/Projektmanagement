

from django.core.management.base import BaseCommand
from django.utils import timezone

from Projektmanagement.models import Project, Task, User

class Command(BaseCommand):
    help = 'Erstellt Beispielprojekte und Aufgaben'

    def handle(self, *args, **kwargs):

        user1 = User.objects.create(firstName='Some', lastName='Body', role='User')
        user2 = User.objects.create(firstName='Another', lastName='One', role='Admin')

        project1 = Project.objects.create(name='Awsome Project', start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=10), notes='Project Notes', owner=user1)
        project2 = Project.objects.create(name='Annoying Project', start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=25), notes='Project Notes', owner=user2)

        Task.objects.create(project=project1, name="Aufgabe 1", description="Beschreibung der Aufgabe 1", project_id=project1.id)
        Task.objects.create(project=project2, name="Aufgabe 2", description="Beschreibung der Aufgabe 2", project_id=project2.id)
        Task.objects.create(project=project1, name="Aufgabe 3", description="Beschreibung der Aufgabe 3", project_id=project1.id)
        Task.objects.create(project=project2, name="Aufgabe 4", description="Beschreibung der Aufgabe 4", project_id=project2.id)
