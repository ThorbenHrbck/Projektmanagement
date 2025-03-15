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
Allgemein verwenden wir in Templates Tags für Variablen und kleinere Logikanteile.
Logik ist aber (bis auf eben einfach for-loops etc. ) meist in der Views Datei angesiedelt. Die View rendert dann die
entsprechenden
Templates und gibt die benötigten Daten als context mit.
Als Konvention haben wir die Namen in der View analog zu den Namen im context und damit in den Templates gehalten. So
kann
z.B. ein

        projects = Project.objects.all().order_by(id)

in der View ausgeführt werden und im context als {'projects': projects} mitgegeben werden
um im Template als Variable {{projects}} genutzt werden zu können.

Wir haben uns zudem entschieden bei Links in den Templates mit URL Pattern Names zu arbeiten um Redundanzen zu vermeiden
und keine Links hardcoden zu müssen. Der Tag dafür sieht dann so aus:

        href="{% url 'project_delete' project_id %}"

Wie hier mit der Project Id sind optionale Parameter ganz einfach mit zu geben.
An einigen Stellen verwenden wir die in Django integrierte ModelForms Klasse um Formulare zum eingeben oder ändern von
Daten nicht in Templates selbst erstellen zu müssen. Diese werden in der View aus den entsprechenden Models erstellt und
als context an die Templates mit gegeben. Die genaue Art des Rendering kann im Template noch angepasst werden (bei uns
werden die Felder als <p> Elemente gerendert). Styling und Validierung der Forms findet in der forms.py selbst statt.

## 2. Seiten

### 2.1 Projekt Übersicht

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
nicht auf der gleichen Seite angezeigt, sondern es wird ein Button (siehe 2.1.1) angezeigt, welcher die nächsten
6 Projekte lädt. Auf der nächsten Seite wird dann auch ein Button zum zurückkehren auf die vorherige Seite angezeigt.
Neben den Buttons zur Navigation wird ein Button zum erstellen eines Projektes angezeigt, welcher zum Template für diese
Aufgabe führt. Dazu verwenden wir die Pagination Klasse von Django in views, wodurch dann jeweils nur die angegebene
Anzahl
an Projekten beim rendern der Seite mit gegeben wird.

### 2.1.1 Button.html

Diese Datei wurde erstellt, um ober und unterhalb der Projektansichten in der Projektübersicht die nachfolgend
beschriebenen Buttons über die von Django gelieferte include option einzubinden und so dopplungen zu vermeiden.
Dies ist eine html Datei welche die Navigation bei mehreren Projekten ermöglicht. Sollten mehr als 6 Projekte vorhanden
sein, erscheint ein Button um die nächsten Projekte zu laden und anzuzeigen. Bei dessen betätigen, werden die ersten 6
nicht mehr, dafür aber die nächsten angezeigt. Auf der "zweiten Seite" wird ein button zum laden der vorherigen Projekte
erscheinen.

## 2.2 Projekt erstellen

Um ein Projekt zu erstellen, wählt man oben im Reiter "Project Create" oder geht unter "Project Overview" auf "Add
Project".
Auf der folgenden Seite wählt bzw. schreibt man dann die Daten zum Projekt. Alle Felder müssen etwas beinhalten. Wenn
man fertig ist, kann man auf "Create" drücken, um den Vorgang abzuschließen. Wenn man auf "Cancel" drückt, wird man
zurück auf die Overview-Seite geleitet.

## 2.3 Projekt aktualisieren.

Um ein Projekt zu aktualisieren, kann man unter "Project Overview" auf "Update" beim jeweiligen Projekt drücken.
Wenn man fertig ist mit den ändern der Daten, drückt man auf "Update", um den Vorgang abzuschließen.

## 2.4 Projekt löschen

Wie bei der Projekt aktualisieren, kann man unter "Project Overview" auf "Delete", bei dem jeweiligen Projekt, drücken.
Wenn man auf "Delete" drückt, wird der Vorgang endgültig abgeschlossen.

## 2.5 Task Übersicht

Diese Seite erscheint wenn man auf der Übersichtsseite der Projekte eines der Projekte anwählt. Auf dieser Seite werden
die dem Projekt zugeordneten Tasks angezeigt. Die Seite benötigt daher als url Parameter zwingend die Projekt-Id.
Die geladenen Tasks des Projektes werden in einzelnen Kacheln angezeigt, sortiert nach dem Datum der Erstellung.

Wenn es mehr als 6 Tasks geben sollte, verwenden wir analog zur Projekt Übersichtsseite die Pagination von Django um nur
die ersten 6 zu laden.
Es wird abhängig von der Seitenzahl ein Button für weitere Tasks oder vorherige Tasks angezeig, was jedes Mal zu einem
rerendern der Seite mit den neuen Daten führt.
Die Tasks zeigen den Namen des Tasks als Überschrift an und geben ansonsten das Start- und Enddatum, die Teilnehmer (als
Dropdown), Details und den Status an. Dieser lässt sich auch auf dieser Seite schon ändern, so das man nicht explizit
den Task updaten muss um ihn als erledigt zu markieren. In jeder Task Kachel gibt es zudem jeweils einen Button zum
Löschen und Ändern des Task.
Über der Darstellun der gesamten Tasks des Projektes befindet sich zusätzlich ein Button um einen neuen Task im Projekt
zu erstellen.

## 2.6 Task erstellen

Diese Seite wird zu einem großen Teil über Djangos ModelForms erstellt. Die benötigten Felder werden dem Formular
mitgegeben und dann als Eingabefelder gerendert.
Die einzigen Pflichtfelder dabei sind der Name und das Projekt, so dass auch schon leere Hülsen für das spätere befüllen
angelegt werden können. Die Mitarbeitenden im Projekt ("Participants") können dabei ebenso wie das Projekt nur aus
bereits bestehenden Einträgen gewählt werden.

## 2.7 Task aktualisiern

Auch diese Seite profitiert von Djangos ModelForms. Die Felder werden im der forms.py definiert und dann als bereits vor
befüllte Eingabefelder gerendert.
Die einzigen Pflichtfelder dabei sind wieder der Name und das Projekt.

## 2.8 Task löschen

Bei Anwählen des Löschen Buttons auf der Task Übersichtseite gibt es eine Weiterleitung zu einer Bestätigungsseite.
Auf dieser muss man das Löschen des Task entweder durch Klick auf den Löschen Button bestätigen oder mit dem Abbruch
Button zurück auf die Übersichtsseite gehen.

# 3. Django Admin Seite

Um auf die Django Admin-Seite zu kommen, gibt man "http://127.0.0.1:8000/admin/" in der Suchleiste bei laufenden
Server ein. Die Anmeldedaten für den Admin sind in der "README.md". Auf der Adminseite angekommen, kann man die
Datenbankeinträge verwalten. Bei der Django Admin Seite nutzen wir die standardmässig voll integrierte Funktionalität
von Django.

# 4. Nutzerverwaltung

Ist momentan leider nicht vollständig implementiert.
Anmelden kann man sich momentan nur als admin und das Konto
wird als Verifizierung des Nutzers momentan nicht verwendet.

# 5. Soll und Ist Vergleich

Wir haben zu Beginn des Projektes folgende Punkte als Must-Haves festgelegt:

1. Projekte können erstellt, verändert (Namen z.B. wenn ein Typo gemacht wurde), und gelöscht werden
2. Ein Projekt umfasst mehrere Aufgaben, sowie Zeitangaben wie Start- und Enddatum. Ein Projekt hat einen Namen. Ein
   Notiz oder Detailsfeld.
3. User können Aufgaben zugewiesen werden
4. User können Aufgaben in Projekten erstellen, ändern und löschen und als abgeschlossen markieren.
5. Verschiedene Benutzerrollen (Projektmanager, User / Mitarbeiter, Admins)
6. Admins haben alle Rechte von Managern und können Rechte vergeben ( Aufstieg von Usern zu Managern und andersherum)

Unsere Nice-To-Haves waren:

- Dark-Mode
- Ein Basetemplate (z.B. ein Corporate Design) haben
- Terminkalender
- Historie
- Verknüpfungen zu Code-Verwaltungstools (z.B. GitHub)
- Sprints

Den ersten Punkt der Must-Haves können wir als vollständig erfüllt sehen. Projekte können neu erstellt werden (siehe
2.2), aktualisert (siehe 2.3) und gelöscht werden (siehe 2.4).

Der zweite Punkt ist ebenso erfolgreich abgeschlossen.
Projekte beinhalten verschiedene Aufgaben, welche wiederum selbst erstellt (siehe 2.6), bearbeitet (siehe 2.7) und
gelöscht (siehe 2.8) werden können.

Das Modell des Projekts enthält dabei selbst keine Beziehung zum Model Tasks. Die Beziehung wird vielmehr über den
Fremdschlüssel im Model Task abgebildet. Die Beziehung zum Owner des Projektes wird über einen Fremdschlüssel zur User
Tabelle dargestellt. Der Owner des Projektes kann daher beim Erstellen eines Projektes aus der Liste der gespeicherten
Nutzer ausgweählt und zugewiesen werden.

Das Zuweisen von Usern zu Aufgaben, das dritte Must-Have haben wir ebenfalls implementiert. Während einem Projekt nur
ein Besitzer zugewisen werden kann, ist die Beziehung zwischen Task und User im Model jeweils als many-to-many beziehung
angelegt.
Dies sorgt für eine etwas anspruchsvollere Behandlung der Beziehungen, vor allem bei der Darstellung auf der Task
Übersichtsseite.
Dort werden sowohl alle Tasks eines Projektes, als auch alle Mitarbeitenden des jeweiligen Tasks dargestellt. Das
Zuweisen von Nutzern zu Tasks kann sowohl direkt beim Erstellen als auch später bei Änderungen eines Tasks passieren.
Ebenso ist es möglich Nutzer wieder von einem Task zu enfernen.

Viertens wollten wir das erstellen, ändern, löschen und als Abgeschlossen markieren von Aufgaben (Tasks) ermöglichen.
Auch das ist uns in vollem Ummfang gelungen. Dabei kann ein Task sowohl auf der Task Übersicht Seite mit einem Toggle
als abeschlossen markiert werden als auch über das Formular zum Ändern von Tasks.

Den fünften Punkt und damit einhergehend den sechsten konnten wir leider nicht komplett erfolgreich abschliessen. Zwar
gibt es
einen SuperUser als Admin und über die Django Klassen auch die Option mehrere Admins zu erstellen. Doch die Nutzer moit
weniger Berechtigungen haben wir leider nicht mehr umsetzen können.

Von den Nice-to-Haves haben wir ein BaseTemplate umgesetzt, welches auf all unseren anderen Template Seiten als
einheitliches Designgerüst dient. Eine Basis für das Umsetzen von Sprintplanungen in Gestalt eines Models haben wir
ebenfalls implementiert, die Umsetzung bleibt aber eine Aufgabe für die Zukunft.











