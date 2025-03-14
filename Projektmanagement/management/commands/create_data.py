from django.core.management.base import BaseCommand
from django.utils import timezone

from Projektmanagement.models import Project, Task, User


class Command(BaseCommand):
    help = 'Erstellt Beispielprojekte und Aufgaben'

    def handle(self, *args, **kwargs):
        user1 = User.objects.create(firstName='Some', lastName='Body', role='User')
        user2 = User.objects.create(firstName='Another', lastName='One', role='Admin')
        user3 = User.objects.create(firstName='Number', lastName='Two', role='User')
        user4 = User.objects.create(firstName='One', lastName='Person', role='User')

        project1 = Project.objects.create(name='Awsome Project', start_date=timezone.now(),
                                          end_date=timezone.now() + timezone.timedelta(days=10),
                                          notes='Project notes of awsome project',
                                          owner=user1)
        project2 = Project.objects.create(name='Annoying Project', start_date=timezone.now(),
                                          end_date=timezone.now() + timezone.timedelta(days=25),
                                          notes='Project notes of annoying project',
                                          owner=user2)
        project3 = Project.objects.create(name='Some Project', start_date=timezone.now() + timezone.timedelta(days=100),
                                          end_date=timezone.now() + timezone.timedelta(days=185),
                                          notes='Project notes of some project',
                                          owner=user3)
        project4 = Project.objects.create(name='This Project', start_date=timezone.now() + timezone.timedelta(days=12),
                                          end_date=timezone.now() + timezone.timedelta(days=25),
                                          notes='Project notes of this project',
                                          owner=user4)
        project5 = Project.objects.create(name='Next Project', start_date=timezone.now(),
                                          end_date=timezone.now() + timezone.timedelta(days=400),
                                          notes='Project notes of next project',
                                          owner=user1)
        project6 = Project.objects.create(name='Big Project', start_date=timezone.now(),
                                          end_date=timezone.now() + timezone.timedelta(days=2000),
                                          notes='Project notes of big project',
                                          owner=user2)
        project7 = Project.objects.create(name='Important Project', start_date=timezone.now(),
                                          end_date=timezone.now() + timezone.timedelta(days=15),
                                          notes='Project notes of important project',
                                          owner=user4)

        task1 = Task.objects.create(project=project1, name="Aufgabe 1", start_date=timezone.now(),
                                    end_date=timezone.now() + timezone.timedelta(days=10),
                                    description="Beschreibung der Aufgabe 1",
                                    project_id=project1.id)
        task1.participants.set({user1, user2, user3, user4})

        task2 = Task.objects.create(project=project2, name="Aufgabe 2", start_date=timezone.now(),
                                    end_date=timezone.now() + timezone.timedelta(days=10),
                                    description="Beschreibung der Aufgabe 2",
                                    project_id=project2.id)
        task2.participants.set({user1, user2, user3, user4})

        task3 = Task.objects.create(project=project1, name="Aufgabe 3", start_date=timezone.now(),
                                    end_date=timezone.now() + timezone.timedelta(days=10),
                                    description="Beschreibung der Aufgabe 3",
                                    project_id=project1.id)
        task3.participants.set({user1, user2, user3, user4})

        task4 = Task.objects.create(project=project2, name="Aufgabe 4", start_date=timezone.now(),
                                    end_date=timezone.now() + timezone.timedelta(days=10),
                                    description="Beschreibung der Aufgabe 4",
                                    project_id=project2.id)
        task4.participants.set({user1, user2, user4})

        task5 = Task.objects.create(project=project3, name="Aufgabe 5", start_date=timezone.now(),
                                    end_date=timezone.now() + timezone.timedelta(days=12),
                                    description="Beschreibung der Aufgabe 5",
                                    project_id=project3.id)
        task5.participants.set({user2, user3, user4})

        task6 = Task.objects.create(project=project3, name="Aufgabe 6", start_date=timezone.now(),
                                    end_date=timezone.now() + timezone.timedelta(days=10),
                                    description="Beschreibung der Aufgabe 6",
                                    project_id=project3.id)
        task6.participants.set({user1, user2, user3, user4})

        task7 = Task.objects.create(project=project3, name="Aufgabe 7", start_date=timezone.now(),
                                    end_date=timezone.now() + timezone.timedelta(days=10),
                                    description="Beschreibung der Aufgabe 7",
                                    project_id=project3.id)
        task7.participants.set({user3, user4})

        task8 = Task.objects.create(project=project3, name="Aufgabe 8", start_date=timezone.now(),
                                    end_date=timezone.now() + timezone.timedelta(days=100),
                                    description="Beschreibung der Aufgabe 8",
                                    project_id=project3.id)
        task8.participants.set({user1, user3, user4})

        task9 = Task.objects.create(project=project4, name="Aufgabe 9", start_date=timezone.now(),
                                    end_date=timezone.now() + timezone.timedelta(days=10),
                                    description="Beschreibung der Aufgabe 7",
                                    project_id=project4.id)
        task9.participants.set({user3, user4})

        task10 = Task.objects.create(project=project4, name="Aufgabe 9", start_date=timezone.now(),
                                     end_date=timezone.now() + timezone.timedelta(days=10),
                                     description="Beschreibung der Aufgabe 7",
                                     project_id=project4.id)
        task10.participants.set({user1, user2, user3, user4})
