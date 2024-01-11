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
