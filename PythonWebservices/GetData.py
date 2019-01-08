import requests
import json
import jsonpath

baseURL = "https://reqres.in/"
req = "/api/users?page=2"

response = requests.get(baseURL+req)
print(response.text)
print(response.content)
print(response.status_code)
