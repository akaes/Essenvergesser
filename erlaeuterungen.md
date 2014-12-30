#Erläuterungen

###Testumgebung: 
Mac OS X mit Python 3.4

##Aufgabenstellung: 
Täglich gegen 12:00 Uhr soll automatisch ein Tweet abgesendet werden, der mit unterschiedlichen Texten an das Mittagessen erinnert.

##Umsetzung:
Python-Script, automatischer Versand des Textes über die Twitter-API.

##Voraussetzungen:
* Twitter-Account

##Vorgehen:
* Anlegen eines Twitter-Accounts
* Registrierung für die Nutzung der Twitter-API 
* Erzeugen der erforderlichen Schlüssel für das OAuth-Verfahren und Registrierung der Anwendung
* Festlegen der Texte für die Auswahl
* Anpassen des Python-Scripts
* Einrichten eines cronJobs (Beispiel für Mac OS X: xml-plist für launchd) auf einem Server

##Dateien:
essenvergesser.py - Pythonscript für den automatischen Versand eines Tweets
beispiel.plist - XML-Datei (Beispiel) für launchd (Speicherort: /Library/LaunchDaemons/)



