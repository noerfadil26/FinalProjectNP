#replace http://localhost:58000 with your network controller's IP address
#insert your setting in (insert_....) without ()
import requests
import json
api_url = "http://localhost:58000/api/v1/network-device"
headers = {
  'X-Auth-Token': '(insert_your_service-ticket_here)',
  'Content-Type': 'application/json'
}
body_json = {
  "ipAddress": "(insert_your_network-device-IP_here)",
  "globalCredentialId": "(insert_your_globalCredentialIdList_here)"
}
resp = requests.post(api_url,json.dumps(body_json), headers=headers, verify=False)
print(resp.text)