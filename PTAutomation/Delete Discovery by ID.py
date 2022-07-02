import requests
import json

url = "http://localhost:58000/api/v1/discovery/1"

payload = json.dumps(1)
headers = {
  'X-Auth-Token': 'NC-8-080562329a864ccf8225-nbi',
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
