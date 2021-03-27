cpu-director Installation

#Datei im Editor öffnen:

sudo nano /home/pi/cpu-director/cpu-temperature.py

#In der Datei bitte die Ziel-URL der API hinterlegen.
#Datei speichern und schließen.

#Damit das Programm automatisch startet sollte das Programm in den systemweiten Crontabs hinterlegt werden.
#Systemweite Crontabs öffnen
sudo nano /etc/crontab

#Folgender Befehl startet den cpu-director automatisch
@reboot sudo python3 /home/pi/cpu-director.py

#System neustarten

sudo reboot

#viel Spaß damit!
