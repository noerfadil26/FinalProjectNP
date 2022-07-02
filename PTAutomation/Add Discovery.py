import requests
import json

api_url = "http://localhost:58000/api/v1/discovery"

headers = {'X-Auth-Token': 'NC-8-080562329a864ccf8225-nbi',
            'Content-Type': 'application/json'}
body_json = {
  "cdpLevel": "16",
  "retry": "3",
  "globalCredentialIdList": [
    "dd9a6dd3-bf3d-4cb4-b84c-1643e290f339"
  ],
  "timeout": "5",
  "ipAddressList": "192.168.1.1",
  "discoveryType": "CDP",
  "name": "OFFICE"
}

response = requests.post(api_url,json.dumps(body_json), headers=headers)

print(response.text)
