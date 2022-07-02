import requests
import json

api_url = "http://localhost:58000/api/v1/global-credential/cli"
headers = {
  'X-Auth-Token': 'NC-8-380f38c01ed343e5b0f4-nbi',
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
