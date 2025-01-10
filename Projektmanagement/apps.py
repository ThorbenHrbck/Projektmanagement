from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Projektmanagement'

    def ready(self):
        # Gruppen erstellen
        from django.contrib.auth.models import Group
        groups = ["Projektmanager", "Mitarbeiter"]
        for group_name in groups:
            Group.objects.get_or_create(name=group_name)