import requests
import json
import jsonpath
# Api Url With id which resource you want to update
url = "https://reqres.in/api/users/2"
# Read Input JSON file
file = open('Update_Users.json','r')
json_input_str = file.read()
request_json = json.loads(json_input_str)
# Make a PUT request
response = requests.put(url,request_json)
print(response.content)
# Parse
response_json = json.loads(response.text)
print(response_json)
# specific content for validation
updated_li = jsonpath.jsonpath(response_json,"updatedAt")
print(updated_li[0])
# Response Code Validation
assert response.status_code == 200



