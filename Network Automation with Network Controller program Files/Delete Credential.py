#replace http://localhost:58000 with your network controller's IP address
#insert your setting in (insert_....) without ()
import requests
import json
api_url = "http://localhost:58000/api/v1/global-credential/(insert_your_credential-ID_here)"
payload = "(insert_your_credential-ID_here)"
headers = {
  'X-Auth-Token': '(insert_your_service-ticket_here)',
  'Content-Type': 'application/json'
}
response = requests.request("DELETE", api_url, headers=headers, data=payload, verify=False)
print(response.text)
