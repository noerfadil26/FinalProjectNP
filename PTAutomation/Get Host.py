import json
import requests
api_url = "http://localhost:58000/api/v1/host"
headers={
    "X-Auth-Token": "NC-8-380f38c01ed343e5b0f4-nbi"}
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
