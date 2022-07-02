import requests
import json
api_url = "http://localhost:58000/api/v1/global-credential/8576d8cc-8baa-4214-91b5-717ce181a673"
payload = "8576d8cc-8baa-4214-91b5-717ce181a673"
headers = {
  'X-Auth-Token': 'NC-7-5924317466424992b3f2-nbi',
  'Content-Type': 'application/json'
}
response = requests.request("DELETE", api_url, headers=headers, data=payload, verify=False)
print(response.text)
