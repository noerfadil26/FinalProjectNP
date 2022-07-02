import requests
import json
api_url = "http://localhost:58000/api/v1/discovery"
headers = {
  'X-Auth-Token': 'NC-7-e3ea509862db4131b1b6-nbi',
  'Content-Type': 'application/json'
}
body_json = {
  "cdpLevel": "16",
  "retry": "3",
  "globalCredentialIdList": [
    "20b54cec-2b78-44b3-9ce7-664c201180d0"
  ],
  "timeout": "5",
  "ipAddressList": "192.168.1.1",
  "discoveryType": "CDP",
  "name": "OFFICE"
}
response = requests.post(api_url,json.dumps(body_json), headers=headers, verify=False)
print(response.text)
