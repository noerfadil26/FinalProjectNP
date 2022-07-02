import requests
import json

api_url = "http://localhost:58000/api/v1/global-credential/cli"
headers = {
  'X-Auth-Token': 'NC-7-5924317466424992b3f2-nbi',
  'Content-Type': 'application/json'
}
body_json = {
  "password": "project",
  "username": "final",
  "enablePassword": "project",
  "description": "TESTING2"
}
response = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)
print(response.text)
