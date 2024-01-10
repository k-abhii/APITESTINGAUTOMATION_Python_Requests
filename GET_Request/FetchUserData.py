import requests

# API URL
url = "https://reqres.in/api/users?page=2"

#Send Get Request
response = requests.get(url)
print(response)

# Display Response Content
print(response.content)
# Display Response Headers
print(response.headers)

# Validate Status Code
assert response.status_code ==200