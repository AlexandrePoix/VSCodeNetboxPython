import requests
import json

url = "<https://yoururl/api/ipam/vlans/>"

payload = json.dumps({
  "vid": "<YourVlanID>",
  "name": "<YourVlanName>",
  "tenant": "<YourTenantID>"
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Token <YOUR_TOKEN_API>',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
