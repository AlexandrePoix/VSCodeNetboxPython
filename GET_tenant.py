import requests
import json

url = "https://demo.netbox.dev/api/tenancy/tenants/"

payload={}
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Token a75dea885edbf297a849e321d1f748bca889027d',
  'Cookie': 'csrftoken=PG9P7OdJEEVYjGvX9p84KF7iSrzlqEN4BlFjC8Stz5y5XHOBUW65WtO1uY3BNI1y'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)