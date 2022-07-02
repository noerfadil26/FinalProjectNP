import requests
import json
api_url = "http://localhost:58000/api/v1/global-credential/cli"
headers = {
  'X-Auth-Token': 'NC-7-5924317466424992b3f2-nbi'
}
resp = requests.get(api_url, headers=headers, verify=False)
response_json = resp.json()
credentials = response_json["response"]
print("Description   \t", "ID\t")
for cred in credentials:
  print(cred["description"],"   \t", cred["id"])
#print(resp.text)
