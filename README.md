cpu-director Installation

#Datei im Editor öffnen:

sudo nano /home/pi/cpu-director/cpu-temperature.py

#In der Datei bitte die Ziel-URL der API hinterlegen.
#Datei speichern und schließen.

#Damit das Programm automatisch startet sollte das Programm in den Crontabs hinterlegt werden.
#Crontabs öffnen

crontab -e

#Folgender Befehl startet den cpu-director automatisch

@reboot python3 /home/pi/cpu-director/cpu-temperature.py

#System neustarten

sudo reboot

#viel Spaß damit!
