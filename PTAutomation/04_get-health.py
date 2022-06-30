import json
import requests
api_url = "http://localhost:58000/api/v1/assurance/health"

headers={"X-Auth-Token": "NC-7-222032b35d6d4e9d96b2-nbi"}

resp = requests.get(api_url, headers=headers, verify=False)

print("Request status: ", resp.status_code)

response_json = resp.json()
health = response_json["response"]

for host in health:
    print(host["clients"]["totalConnected"],"\t", host["clients"]["totalPercentage"])
