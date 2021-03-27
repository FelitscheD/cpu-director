#Erstellt von FelitscheD
#Version 1.0
#Liest die CPU des Raspberry Pi 4 aus
#Streamt diese an die API eines Livedatasets von Power BI
 
import json
import traceback
import urllib
from datetime import datetime
import urllib.request

header = {"Content-Type": "application/json; charset=utf-8"}
url = "***Url-API***"

while True:
 try:
#CPU-Temperatur auslesen und schreiben
  tempData = "/sys/class/thermal/thermal_zone0/temp"
  dateilesen = open(tempData, "r")
  temperature = dateilesen.readline(2)
  dateilesen.close()
  print(temperature)
#Zeitstempel erstellen und schreiben
  now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
  timestamp = now
  print(timestamp)
#JSON für Power BI API erstellen
  formdata = {
      "temperature": (temperature),
      "timestamp": (timestamp)
}
  data = json.dumps(formdata)
  data = json.dumps(formdata).encode()


  request = urllib.request.Request(url, data, header)
    # Output string
  response = urllib.request.urlopen(request)
  response_str = response.read()
  response.close()
  print(response_str)
 except urllib.error.HTTPError as e:
    print("The server couldn't fulfill the request")
    print(e.code)
    print(e.read())
 except urllib.error.URLError as e:
    print("Failed to reach the server")
    print(e.reason)
 except:
    traceback.print_exc()
