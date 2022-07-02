import json
from urllib import response
import requests
api_url = "http://localhost:58000/api/v1/network-device"

headers={"X-Auth-Token": "NC-8-080562329a864ccf8225-nbi"}

resp = requests.get(api_url, headers=headers, verify=False)

print("Request status: ", resp.status_code)

response_json = resp.json()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    print(networkDevice["type"], "\t", networkDevice["hostname"], "\t", networkDevice["productId"], "\t", networkDevice["managementIpAddress"], "\t",networkDevice["softwareVersion"])

