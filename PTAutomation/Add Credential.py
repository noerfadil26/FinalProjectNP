import requests
import json
import pandas as pnd


api_url = "http://localhost:58000/api/v1/global-credential/cli"

headers = {
  'X-Auth-Token': 'NC-20-0db373c89ac14fdea07b-nbi',
  'Content-Type': 'application/json'
}
body_json = {
  "password": "project",
  "username": "last",
  "enablePassword": "project",
  "description": "TESTING2"
}
resp = requests.post(api_url,json.dumps(body_json),headers=headers)
response_json = resp.json()
credential=response_json
print (" id\t:\t",credential["id"],"\n","username:\t",credential["username"],"\n","password:\t",credential["password"],"\n","enable password:\t",credential["enablePassword"])