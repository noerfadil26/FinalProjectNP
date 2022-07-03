#replace http://localhost:58000 with your network controller's IP address
#insert your setting in (insert_....) without ()
import requests
import json
api_url = "http://localhost:58000/api/v1/global-credential/cli"
headers = {
  'X-Auth-Token': '(insert_your_service-ticket_here)'
}
resp = requests.get(api_url, headers=headers, verify=False)
response_json = resp.json()
credentials = response_json["response"]
print("Description   \t", "ID\t")
for cred in credentials:
  print(cred["description"],"   \t", cred["id"])