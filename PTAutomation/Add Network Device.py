import requests
import json
api_url = "http://localhost:58000/api/v1/network-device"
headers = {
  'X-Auth-Token': 'NC-8-380f38c01ed343e5b0f4-nbi',
  'Content-Type': 'application/json'
}
body_json = {
  "ipAddress": "192.168.10.14",
  "globalCredentialId": "28e73115-c45e-41ea-bf47-85f1ce868c4e"
}
resp = requests.post(api_url,json.dumps(body_json), headers=headers, verify=False)
print(resp.text)