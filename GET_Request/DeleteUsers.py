import requests

# API URL
url = "https://reqres.in/api/users/2"
response = requests.delete(url)
#FETCH RESPONSE CODE
print(response.status_code)
assert response.status_code ==204
