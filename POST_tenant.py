import requests
import json

url = "https://demo.netbox.dev/api/tenancy/tenants/"

payload = json.dumps({
  "name": "agrotestvscpython",
  "slug": "agrotestvscpython"
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Token a75dea885edbf297a849e321d1f748bca889027d',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
