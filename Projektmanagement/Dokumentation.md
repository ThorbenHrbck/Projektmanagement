1. Projekt:
1.1 Projekt Übersicht
Dient der ÜBersicht für alle erstellten Projekte. Dabei werden Name des Projektes als fettgeschriebene Überschrift, Start- und Enddatum, Besitzer des Projektes und eine Projektbeschreibung angezeigt. Die Projektbeschreibung ist dabei ein Feld mit einer maximalgröße von 20 Zeichen, damit dessen größe das Designe nicht zu groß verändert, da es ansonsten das div vergrößern würde. Innerhalb der anzeige von einem Projekt gibt es noch einen Update und delete button, welchen zu den jeweiligen Templates mit den übergebenen Projekten führt. Sollten mehr als 6 Projekte vorhanden sein werden diese nicht auf der gleichen Seite angezeigt, sondern es wird ein button (beschreibung 1.1.2) angezeigt, welcher die nächsten 6 Projekte lädt. Auf der nächsten Seite wird dann auch ein Button zum zurückkehren auf die vorherige Seite angezeigt.
Neben den Buttons zur Navigation wird ein Button zum erstellen eines Projektes angezeigt, welcher zum Template für diese Aufgabe führt.
1.1.2 Button.html
Diese Datei wurde erstellt, um ober und unterhalb der Projektansichten in der Projektübersicht die nachfolgend beschriebenen Buttons über die von Django gelieferte include option einzubinden und so dopplungen zu vermeiden.
Dies ist eine html Datei welche die Navigation bei mehreren Projekten ermöglicht. Sollten mehr als 6 Projekte vorhanden sein, erscheint ein Button um die nächsten Projekte zu laden und anzuzeigen. Bei dessen betätigen, werden die ersten 6 nicht mehr dafür aber die nächsten angezeigt. Auf der "zweiten Seite" wird ein button zum laden der vorherigen Projekte erscheinen.

1.2 Projekt erstellen
Um ein Projekt zu erstellen, wählt man oben im Reiter "Project Create". Auf der folgenden Seite wählt bzw. schreibt man dann die Daten zum Projekt. Alle Felder müssen etwas beinhalten. Wenn man fertig ist, kann man auf "Create" drücken, um den Vorgang abzuschließen. Wenn man auf "Cancel" drückt, wird man zurück auf die Overview-Seite geleitet.

1.2 Projekt aktualisieren.
Um ein Projekt zu aktualisieren, kann man das zurzeit nur über einen Link wie folgt: "http://127.0.0.1:8000/projects/update/6/" wobei die 6 die ID in der Datenbank entspricht. Wenn man fertig ist mit den ändern der Daten, drückt man auf "Update", um den Vorgang abzuschließen.

Wie bei der Projekt aktualisieren, kann man die Funktionalität momentan nur über folgenden Link nutzen: "http://127.0.0.1:8000/projects/delete/6/", wobei die 6 wieder für die ID des Projektes spricht. Wenn man auf "Delete" drückt, wird der Vorgang endgültig abgeschlossen.

1.3 Projekt löschen
Wie bei der Projekt aktualisieren, kann man in der Projekt Overview auf das jeweilige Projekt auf "Delete" drücken. Wenn man auf "Delete" drückt, wird der Vorgang endgültig abgeschlossen.
Wie bei der Projekt aktualisieren, kann man die Funktionalität momentan nur über folgenden Link nutzen: "http://127.0.0.1:8000/projects/delete/6/", wobei die 6 wieder für die ID des Projektes spricht. Wenn man auf "Delete" drückt, wird der Vorgang endgültig abgeschlossen.


2. Basetemplate
Diese Datei dient dazu das jedes andere Template ein festgelegten Grundris, mit, für alle seiten benötigten Funktionalitäten, zu bieten. Hierbei werden zwei bereiche festgelegt, ein Kopf- und ein Fußbereich. Im Kopfbereich wird ganz link ein Logo angezeigt, welches auch als Link zur Projektübersicht dient, daneben gibt es ein Dropdown um auf die Seiten Projektübericht und Projekterstellung zu kommen, in der Mitte wird der Projektname angezeigt und ganz rechts gibt es den Logout button. Im Füßbereich wurde ein Copyrite eingefügt. Zwischen diesen beiden wurde {% block content %} und {% endblock %} eingefügt, welches den Ort zum Laden von anderen Templates festlegt. Über {% extends "baseTemplate.html" %} am anfang von anderen Templates, greifen diese auf das Basetemplate zu.