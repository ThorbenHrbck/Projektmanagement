# Projektmanagement

## Neu im Projekt?

Um die SQLite-Datenbank zu erstellen, führe den folgenden Befehl aus:
Achtung: Es kann je nach Entwicklungsumgebung statt python pip oder pthon3 im Befehl nötig sein.

    python manage.py migrate

Bei Bedarf an Testdaten folgenden Befehl ausführen:

    python manage.py create_data

Jetzt kannst du den Django-Entwicklungsserver starten, um das Projekt lokal auszuführen:

    python manage.py runserver

Der Link zur Seite erscheint im Terminal, kann aber auch unter der url http://127.0.0.1:8000/ selbst im Browser
aufgerufen werden.
Wenn auf die Admin Seite zugegriffen werden soll, kann das über http://127.0.0.1:8000/admin
mit den Anmeldedaten

    name: admin
    pw: Admin123456

gemacht werden.

Genauere Informationen finden sich in der Dokumentation.md

### Project Guidelines:

Projektsprache: Englisch
One Task, one Branch

Must-Haves:

    Projekte können erstellt, verändert (Namen z.B. wenn ein Typo gemacht wurde), und gelöscht werden
    Ein Projekt umfasst mehrere Aufgaben, sowie Zeitangaben wie Start- und Enddatum. Ein Projekt hat einen Namen. Ein Notiz oder Detailsfeld.
    User können Projekten zugewiesen werden
    User können Aufgaben in Projekten erstellen, ändern und löschen und als abgeschlossen markieren.
    Verschiedene Benutzerrollen (Projektmanager, User / Mitarbeiter, Admins)
    Admins haben alle Rechte von Managern und können Rechte vergeben ( Aufstieg von Usern zu Managern und andersherum)

Nice-To-Haves

    Dark-Mode
    Ein Basetemplate (z.B. ein Corporate Design) haben
    Terminkalender
    Historie
    Verknüpfungen zu Code-Verwaltungstools (z.B. GitHub)
    Sprints

