import requests
import json

url = "<https://yoururl/api/tenancy/tenants/>"

payload = json.dumps({
  "name": "agrotestvscpython",
  "slug": "agrotestvscpython"
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Token <YourToken>',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
