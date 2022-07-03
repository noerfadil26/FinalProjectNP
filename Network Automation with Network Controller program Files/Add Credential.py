#replace http://localhost:58000 with your network controller's IP address
#insert your setting in (insert_....) without ()
import requests
import json

api_url = "http://localhost:58000/api/v1/global-credential/cli"
headers = {
  'X-Auth-Token': '(insert_your_service-ticket_here)',
  'Content-Type': 'application/json'
}
body_json = {
  "password": "(insert_your_credential-password_here)",
  "username": "(insert_your_credential-username_here)",
  "enablePassword": "(insert_your_enablePassword_here)",
  "description": "(insert_your_credential-description_here)"
}
response = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)
print(response.text)
