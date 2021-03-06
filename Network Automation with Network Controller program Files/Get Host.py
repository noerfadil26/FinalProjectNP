#replace http://localhost:58000 with your network controller's IP address
#insert your setting in (insert_....) without ()
import json
import requests
api_url = "http://localhost:58000/api/v1/host"
headers={
    "X-Auth-Token": "(insert_your_service-ticket_here)"}
resp = requests.get(api_url, headers=headers, verify=False)
print("Request status: ", resp.status_code)
response_json = resp.json()
hosts = response_json["response"]
print("Hostname\t", "IP Address\t", "MAC Address     \t", "Connected Interface")
for host in hosts:
    try:
        print(host["hostName"],"     \t", host["hostIp"], "\t", host["hostMac"], "\t", host["connectedInterfaceName"])
    except KeyError:
        continue
