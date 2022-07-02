import requests
import json
api_url = "http://localhost:58000/api/v1/discovery"
headers = {
  'X-Auth-Token': 'NC-8-380f38c01ed343e5b0f4-nbi',
  'Content-Type': 'application/json'
}
body_json = {
  "cdpLevel": "16",
  "retry": "3",
  "globalCredentialIdList": [
    "79a3a9dc-f89f-4caa-b958-b06eecb07231"
  ],
  "timeout": "5",
  "ipAddressList": "192.168.1.1",
  "discoveryType": "CDP",
  "name": "OFFICE"
}
response = requests.post(api_url,json.dumps(body_json), headers=headers, verify=False)
print(response.text)