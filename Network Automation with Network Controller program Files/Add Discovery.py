#replace http://localhost:58000 with your network controller's IP address
#insert your setting in (insert_....) without ()
import requests
import json
api_url = "http://localhost:58000/api/v1/discovery"
headers = {
  'X-Auth-Token': '(insert_your_service-ticket_here)',
  'Content-Type': 'application/json'
}
body_json = {
  "cdpLevel": "16",
  "retry": "3",
  "globalCredentialIdList": [
    "(insert_your_globalCredentialIdList_here)"
  ],
  "timeout": "5",
  "ipAddressList": "(insert_your_setting_here)",
  "discoveryType": "CDP",
  "name": "OFFICE"
}
response = requests.post(api_url,json.dumps(body_json), headers=headers, verify=False)
print(response.text)