import requests
import json
api_url = "http://localhost:58000/api/v1/discovery/{discoveryid}"
payload = json.dumps({discoveryid})
headers = {
  'X-Auth-Token': 'NC-8-080562329a864ccf8225-nbi',
  'Content-Type': 'application/json'
}
response = requests.request("DELETE", api_url, headers=headers, data=payload, verify=False)
print(response.text)
