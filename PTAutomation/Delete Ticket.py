import requests
import json
api_url = "http://localhost:58000/api/v1/ticket/NC-5-d1d6adf0a618431d9c9c-nbi"
payload = "0NC-5-d1d6adf0a618431d9c9c-nbi"
headers = {
  'X-Auth-Token': 'NC-5-d1d6adf0a618431d9c9c-nbi',
  'Content-Type': 'application/json'
}
response = requests.request("DELETE", api_url, headers=headers, data=payload, verify=False)
print(response.text)
