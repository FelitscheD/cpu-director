import json
import traceback
import urllib
from datetime import datetime
import urllib.request

# 1. First remove urllib2, python3 uses urllib uniformly
# import urllib2

# json data
formdata = {
    "temperature": ("Mist")
}
#data = json.dumps(formdata)
header = {"Content-Type": "application/json; charset=utf-8"}
url = "https://api.powerbi.com/beta/0296808a-c473-4660-bee9-32f20745a5d1/datase$
#data = json.dumps(formdata).encode()

# 2. Modify the statement from urllib2 to urllib conversion
while True:
 try:

  tempData = "/sys/class/thermal/thermal_zone0/temp"
  dateilesen = open(tempData, "r")
  temperature = dateilesen.readline(2)
  dateilesen.close()
  print(temperature)
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
