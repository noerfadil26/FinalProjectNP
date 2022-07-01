import requests
import json
headers = {'X-Auth-Token': 'NC-20-0db373c89ac14fdea07b-nbi','Content-Type': 'application/json'}
api_url = "http://localhost:58000/api/v1/wan/network-wide-setting"
body_json = {
  "ntp": {
    "serverIp": "192.168.1.6"
  },
  "dns": {
    "name": "finalproject.com",
    "ipAddress": "192.168.1.1"
  }
}
resp = requests.put(api_url, json.dumps(body_json), headers=headers,verify=False)
response_json = resp.json()
settings=response_json["response"]
print ("DNS IP Address\t:", settings["dns"]["ipAddress"])
print ("DNS Name\t:", settings["dns"]["name"])
print ("NTP Server IP\t:", settings["ntp"]["serverIp"])
