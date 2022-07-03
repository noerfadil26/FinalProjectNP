import requests
import json

api_url = "http://localhost:58000/api/v1/global-credential/cli"
headers = {
  'X-Auth-Token': 'NC-4-4fe35d1a2aa3498b875a-nbi',
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
