import requests

api_url = "http://localhost:58000/api/v1/discovery"

headers = {
  'X-Auth-Token': 'NC-8-080562329a864ccf8225-nbi'
}

resp = requests.get(api_url, headers=headers)

print(resp.text)
