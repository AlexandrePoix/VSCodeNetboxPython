import requests
import json

url = "<https://yoururl/api/tenancy/tenants/>"

payload={}
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Token <Your_Token_API>'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
