# Projekt:

# 1. Basetemplate und Templating

Das BaseTemplate dient dazu, für jedes andere Template einen festgelegten Grundriss zu bieten der die übergreifend für
alle Seiten benötigten Funktionalitäten mitbringt. Hierbei werden zwei Bereiche festgelegt, ein Kopf- und ein
Fußbereich.
Im Kopfbereich (Header) wird ganz links ein Logo angezeigt, welches auch als Link zur Projektübersicht dient.
Daneben gibt es ein Dropdown um wahlweise auf die Seiten Projektübericht und Projekterstellung zu kommen.
In der Mitte wird der Name der Applikation angezeigt und rechts gibt es den Logout Button. Im unteren Teil (Footer)
wurde ein Hinweis auf unsere Creative Commons Lizenz eingefügt.

Zwischen diesen beiden wurde die Tags {% block content %} und {% endblock %} eingefügt, welche damit den Ort zum Laden
von anderen Templates festlegen.
Über das {% extends "baseTemplate.html" %} Tag am Anfang von anderen Templates greifen diese auf das Basetemplate zu.

## 2. Projekt Übersicht

Um auf diese Seite zu kommen, kann man das Logo oben links in der Ecke oder im Dropdown daneben auf "Project Overview"
clicken.

Dient der Übersicht für alle erstellten Projekte. Dabei werden der Name des Projektes als fettgeschriebene Überschrift,
ausserdem das Start- und Enddatum, Besitzer des Projektes und eine Projektbeschreibung angezeigt. Die
Projektbeschreibung ist ein Feld mit einer Maximalgröße von 20 Zeichen, damit dessen Größe die Anzeige nihct
beeinflusst.
Weitere Inhalte werden mit "..." angedeutet. Innerhalb der Anzeige eines einzelnen Projekts gibt es noch einen Update
und einen Delete Button, welcher
zu den jeweiligen Templates mit den übergebenen Projekten führt.

Sollten mehr als 6 Projekte vorhanden sein werden diese
nicht auf der gleichen Seite angezeigt, sondern es wird ein button (siehe 2.1) angezeigt, welcher die nächsten
6 Projekte lädt. Auf der nächsten Seite wird dann auch ein Button zum zurückkehren auf die vorherige Seite angezeigt.
Neben den Buttons zur Navigation wird ein Button zum erstellen eines Projektes angezeigt, welcher zum Template für diese
Aufgabe führt.

### 2.1 Button.html

Diese Datei wurde erstellt, um ober und unterhalb der Projektansichten in der Projektübersicht die nachfolgend
beschriebenen Buttons über die von Django gelieferte include option einzubinden und so dopplungen zu vermeiden.
Dies ist eine html Datei welche die Navigation bei mehreren Projekten ermöglicht. Sollten mehr als 6 Projekte vorhanden
sein, erscheint ein Button um die nächsten Projekte zu laden und anzuzeigen. Bei dessen betätigen, werden die ersten 6
nicht mehr dafür aber die nächsten angezeigt. Auf der "zweiten Seite" wird ein button zum laden der vorherigen Projekte
erscheinen.

## 2.2 Projekt erstellen

Um ein Projekt zu erstellen, wählt man oben im Reiter "Project Create" oder unter "Project Overview" auf "Add Project".
Auf der folgenden Seite wählt bzw. schreibt man dann die Daten zum Projekt. Alle Felder müssen etwas beinhalten. Wenn
man fertig ist, kann man auf "Create" drücken, um den Vorgang abzuschließen. Wenn man auf "Cancel" drückt, wird man
zurück auf die Overview-Seite geleitet.

## 2.3 Projekt aktualisieren.

Um ein Projekt zu aktualisieren, kann man unter "Project Overview" auf "Update", bei dem jeweiligen Projekt, drücken.
Wenn man fertig ist mit den ändern der Daten, drückt man auf "Update", um den Vorgang abzuschließen.

## 2.4 Projekt löschen

Wie bei der Projekt aktualisieren, kann man unter "Project Overview" auf "Delete", bei dem jeweiligen Projekt, drücken.
Wenn man auf "Delete" drückt, wird der Vorgang endgültig abgeschlossen.

# 3. Django Admin Seite

Um auf die Django Admin-Seite zu kommen, gibt man "http://127.0.0.1:8000/admin/" in der Suchleiste bei laufenden
Server ein. Die Anmeldedaten für den Admin sind in der "README.md". Auf der Adminseite angekommen, kann man die
Datenbankeinträge verwalten.

# 4. Nutzerverwaltung

Die ist momentan leider nicht vollständig implementiert. Anmelden kann man sich momentan nur als admin und das Konto
wird als Verifizierung des Nutzers momentan nicht verwendet.