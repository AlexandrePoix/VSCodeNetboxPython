import requests
import json

url = "<https://yoururl/api/tenancy/tenants/>"

payload = json.dumps({
  "name": "<name_of_the_new_tenant>",
  "slug": "<name_of_the_new_tenant>"
})
headers = {
  'accept': 'application/json',
  'Authorization': 'Token <Your_Token_API>',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
