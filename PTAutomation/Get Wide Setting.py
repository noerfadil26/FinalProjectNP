import requests
import json

api_url = "http://localhost:58000/api/v1/wan/network-wide-setting"

json_body = ""
headers = {
  'X-Auth-Token': 'NC-8-080562329a864ccf8225-nbi'
}

response = requests.get(api_url, json.dumps(json_body),headers=headers)

print(response.text)
