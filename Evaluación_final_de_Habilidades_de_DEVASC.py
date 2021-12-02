import requests
import json


print("######################################################")
print("####     Step 2: Get the Organization ID          ####")
print("######################################################\n")


api_url='https://api.meraki.com/api/v1/organizations'
headers={'X-Cisco-Meraki-API-Key':'6bec40cf957de430a6f1f2baa056b99a4fac9ea0','Accept':'application/json','Content-Type': 'application/json'}
print(api_url)

resp = requests.get(api_url,headers=headers,verify=True)
print("Response status:",resp.status_code)


resp_organizationId = resp.json()
organizationId = resp_organizationId[0]['id']
print(json.dumps(resp.json(),indent=2))


print("######################################################")
print("#### Step 3: Get the networks in the organization ####")
print("######################################################\n")


URL=(f"https://api.meraki.com/api/v1/organizations/{organizationId}/networks")
print(URL)


api_url= URL
headers={'X-Cisco-Meraki-API-Key':'6bec40cf957de430a6f1f2baa056b99a4fac9ea0','Accept':'application/json','Content-Type': 'application/json'}


resp = requests.get(api_url,headers=headers,verify=True)
print("Response status:",resp.status_code)


resp_organizationId = resp.json()
networkId = resp_organizationId[0]['id']
print(json.dumps(resp.json(),indent=2))


print("######################################################")
print("####      Step 4: Get the devices in a network    ####")
print("######################################################\n")


URL=(f"https://api.meraki.com/api/v1/networks/{networkId}/devices")
print(URL)


api_url= URL
headers={'X-Cisco-Meraki-API-Key':'6bec40cf957de430a6f1f2baa056b99a4fac9ea0','Accept':'application/json','Content-Type': 'application/json'}


resp = requests.get(api_url,headers=headers,verify=True)
print("Response status:",resp.status_code)


serial = resp.json()
networkId = serial[2]['networkId']
print(json.dumps(resp.json(),indent=2))


serial=serial[0]['serial']


print("######################################################")
print("####        Step 5: Get network information       ####")
print("######################################################\n")


URL=(f'https://api.meraki.com/api/v1/networks/{networkId}')
print(URL)


api_url=URL
headers={'X-Cisco-Meraki-API-Key':'6bec40cf957de430a6f1f2baa056b99a4fac9ea0','Accept':'application/json','Content-Type': 'application/json'}


resp = requests.get(api_url,headers=headers,verify=True)
print("Response status:",resp.status_code)


print(json.dumps(resp.json(),indent=2))


print("######################################################")
print("####       Step 6: Get device information         ####")
print("######################################################\n")


URL=(f'https://api.meraki.com/api/v1/networks/{networkId}/devices/{serial}')
print(URL)


api_url=URL
headers={'X-Cisco-Meraki-API-Key':'6bec40cf957de430a6f1f2baa056b99a4fac9ea0','Accept':'application/json','Content-Type': 'application/json'}


resp = requests.get(api_url,headers=headers,verify=True)
print("Response status:",resp.status_code)


print(json.dumps(resp.json(),indent=2))


print("######################################################")
print("####        Step 7: Get SSID information          ####")
print("######################################################\n")


URL=(f'https://api.meraki.com/api/v1/networks/{networkId}/wireless/ssids')
print(URL)


api_url=URL
headers={'X-Cisco-Meraki-API-Key':'6bec40cf957de430a6f1f2baa056b99a4fac9ea0','Accept':'application/json','Content-Type': 'application/json'}


resp = requests.get(api_url,headers=headers,verify=True)
print("Response status:",resp.status_code)


networkId = resp.json()
print(json.dumps(resp.json(),indent=2))

