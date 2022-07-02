import requests
import json
api_url = "http://localhost:58000/api/v1/global-credential/cli"
headers = {
  'X-Auth-Token': 'NC-8-380f38c01ed343e5b0f4-nbi'
}
resp = requests.get(api_url, headers=headers, verify=False)
response_json = resp.json()
credentials = response_json["response"]
print("Description   \t", "ID\t")
for cred in credentials:
  print(cred["description"],"   \t", cred["id"])