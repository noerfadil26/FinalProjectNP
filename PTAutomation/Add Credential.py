import requests
import json

api_url = "http://localhost:58000/api/v1/global-credential/cli"
headers = {
  'X-Auth-Token': 'NC-7-e3ea509862db4131b1b6-nbi',
  'Content-Type': 'application/json'
}
body_json = {
  "password": "project",
  "username": "final",
  "enablePassword": "project",
  "description": "OFFICE"
}
response = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)
print(response.text)
