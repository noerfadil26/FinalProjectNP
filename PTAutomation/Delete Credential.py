import requests
import json
api_url = "http://localhost:58000/api/v1/global-credential/79a3a9dc-f89f-4caa-b958-b06eecb07231"
payload = "79a3a9dc-f89f-4caa-b958-b06eecb07231"
headers = {
  'X-Auth-Token': 'NC-8-380f38c01ed343e5b0f4-nbi',
  'Content-Type': 'application/json'
}
response = requests.request("DELETE", api_url, headers=headers, data=payload, verify=False)
print(response.text)
