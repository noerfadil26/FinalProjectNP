#replace http://localhost:58000 with your network controller's IP address
#insert your setting in (insert_....) without ()
import requests
import json
api_url = "http://localhost:58000/api/v1/discovery"
headers = {
  'X-Auth-Token': '(insert_your_service-ticket_here)'
}
resp = requests.get(api_url, headers=headers)
response_json = resp.json()
discoveries = response_json["response"]
print("Status   \t", "ID\t", "Condition\t", "Name")
for disc in discoveries:
  print(disc["discoveryStatus"],"   \t", disc["id"], "\t", disc["discoveryCondition"], "\t", disc["name"])