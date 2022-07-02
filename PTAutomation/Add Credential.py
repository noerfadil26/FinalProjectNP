import requests
import json
api_url = "http://localhost:58000/api/v1/global-credential/cli"
headers = {
  'X-Auth-Token': 'NC-8-080562329a864ccf8225-nbi',
  'Content-Type': 'application/json'
}
body_json = {
  "password": "project",
  "username": "final",
  "enablePassword": "project",
  "description": "CRED2"
}
resp = requests.post(api_url,json.dumps(body_json),headers=headers)
response_json = resp.json()
credential=response_json
print (" id\t:\t",credential["id"],"\n","username:\t",credential["username"],"\n","password:\t",credential["password"],"\n","enable password:\t",credential["enablePassword"])