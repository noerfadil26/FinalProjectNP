import requests
import json
api_url = "http://localhost:58000/api/v1/discovery"
headers = {
  'X-Auth-Token': 'NC-4-4fe35d1a2aa3498b875a-nbi',
  'Content-Type': 'application/json'
}
body_json = {
  "cdpLevel": "16",
  "retry": "3",
  "globalCredentialIdList": [
    "96f3a3e5-8235-4239-bda5-d5652f2bebee"
  ],
  "timeout": "5",
  "ipAddressList": "192.168.1.1",
  "discoveryType": "CDP",
  "name": "OFFICE"
}
response = requests.post(api_url,json.dumps(body_json), headers=headers, verify=False)
print(response.text)