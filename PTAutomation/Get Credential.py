from urllib import response
import requests
import json

api_url = "http://localhost:58000/api/v1/global-credential/cli"

body_json = ""
headers = {
  'X-Auth-Token': 'NC-8-080562329a864ccf8225-nbi'
}

resp = requests.get(api_url, json.dumps(body_json), headers=headers,verify=False)
response_json = resp.json()
credentials=response_json["response"]
for credential in credentials:
    print (" Description:\t",credential["description"],"\n","ID:\t",credential["id"],"\n",)
#print(resp.text)
