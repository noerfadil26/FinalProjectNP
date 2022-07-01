import json
from urllib import response
import requests
api_url = "http://localhost:58000/api/v1/network-device"

headers={"X-Auth-Token": "NC-17-e88b3ec8dc864a8abbb8-nbi"}

resp = requests.get(api_url, headers=headers, verify=False)

print("Request status: ", resp.status_code)

response_json = resp.json()
networkDevices = response_json["response"]

print(response_json.text)
#for networkDevice in networkDevices:
#    print(networkDevice["type"], "\t", networkDevice["hostname"], "\t", networkDevice["productId"], "\t", networkDevice["managementIpAddress"], "\t",networkDevice["macAddress"], "\t",networkDevice["softwareVersion"])

