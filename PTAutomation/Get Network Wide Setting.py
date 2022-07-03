import requests
import json
api_url = "http://localhost:58000/api/v1/wan/network-wide-setting"
headers = {
  'X-Auth-Token': 'NC-4-4fe35d1a2aa3498b875a-nbi'
}
resp = requests.get(api_url,headers=headers, verify=False)
response_json = resp.json()
settings=response_json["response"]
print ("DNS IP Address\t:", settings["dns"]["ipAddress"])
print ("DNS Name\t:", settings["dns"]["name"])
print ("NTP Server IP\t:", settings["ntp"]["serverIp"])