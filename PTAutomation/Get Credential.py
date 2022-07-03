import requests
import json
api_url = "http://localhost:58000/api/v1/global-credential/cli"
headers = {
  'X-Auth-Token': 'NC-4-4fe35d1a2aa3498b875a-nbi'
}
resp = requests.get(api_url, headers=headers, verify=False)
response_json = resp.json()
credentials = response_json["response"]
print("Description   \t", "ID\t")
for cred in credentials:
  print(cred["description"],"   \t", cred["id"])