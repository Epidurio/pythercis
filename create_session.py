import requests

url = "http://localhost:8080/rest/v1/session"
username = "root"
password = "secret"

querystring = {
    "username": username,
    "password": password
    }

headers = {
    'username': username,
    'password': password,
    'cache-control': "no-cache",
    'postman-token': "f5fefaa7-d9b4-2595-ecd6-a99dcc0f96b3"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)
