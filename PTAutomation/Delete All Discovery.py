import requests
import json
api_url = "http://localhost:58000/api/v1/discovery"
payload = "0NC-5-d1d6adf0a618431d9c9c-nbi"
headers = {
  'X-Auth-Token': 'NC-7-5924317466424992b3f2-nbi',
  'Content-Type': 'application/json'
}
response = requests.request("DELETE", api_url, headers=headers, data=payload, verify=False)
print(response.text)
