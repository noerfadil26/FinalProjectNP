import json
import requests
api_url = "http://localhost:58000/api/v1/network-device"
headers={"X-Auth-Token": "NC-8-380f38c01ed343e5b0f4-nbi"}
resp = requests.get(api_url, headers=headers, verify=False)
print("Request status: ", resp.status_code)
response_json = resp.json()
netDevices = response_json["response"]
print("Hostname\t", "IP Address\t", "Product ID\t","SW Version\t","Status   \t","Type")
for netDev in netDevices:
    print(netDev["hostname"],"    \t", netDev["managementIpAddress"], "\t", netDev["productId"], "\t",netDev["softwareVersion"], "   \t",netDev["reachabilityStatus"],"\t",netDev["type"])