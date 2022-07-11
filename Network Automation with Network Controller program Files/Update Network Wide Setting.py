#replace http://localhost:58000 with your network controller's IP address (for internal access)
#insert your setting in (insert_....) without ()
import requests
import json
headers = {
  'X-Auth-Token': '(insert_your_service-ticket_here)',
  'Content-Type': 'application/json'
}
api_url = "http://localhost:58000/api/v1/wan/network-wide-setting"
body_json = {
  "ntp": {
    "serverIp": "(insert_your_NTP-Server-IP_here)"
  },
  "dns": {
    "name": "(insert_your_DNS-name_here)",
    "ipAddress": "(insert_your_DNS-IP_here)"
  }
}
resp = requests.put(api_url, json.dumps(body_json), headers=headers,verify=False)
response_json = resp.json()
settings=response_json["response"]
print ("DNS IP Address\t:", settings["dns"]["ipAddress"])
print ("DNS Name\t:", settings["dns"]["name"])
print ("NTP Server IP\t:", settings["ntp"]["serverIp"])
