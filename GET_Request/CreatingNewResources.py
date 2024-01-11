import requests
import json
import jsonpath
#API URL---> Base Url + Relative URL here base url = "https://reqres.in/"
url ="https://reqres.in/api/users"
#Read Input Json File--> Replace single slash(\) to (\\)
# file = open("C:\\Users\\hp\\PycharmProjects\\APIAUTOMATIONPYTHON\\GET_Request\\Create_Users.json","r")
file = open("Create_Users.json","r")
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)
# Make POST request with Json Input Body
response = requests.post(url,request_json)
print(response.content)
# Validating Response Code
assert response.status_code ==201
#fetch headers
print(response.headers)
#specific headers
print(response.headers.get("Content-Length"))
# Parse Response To Json Format
response_json = json.loads(response.text)
print(response_json)
# Pick id through jsonpath
id = jsonpath.jsonpath(response_json,'id')  # it will return a list
print(id[0])
