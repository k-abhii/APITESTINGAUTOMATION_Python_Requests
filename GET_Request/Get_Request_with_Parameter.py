import requests
param = {'name':'testingworld','email':'testingworldindia@gmail.com','number':'+91-8743-913121'}
response = requests.get("https://httpbin.org/get",params=param)
print(response.text)

# {
#   "args": {
#     "email": "testingworldindia@gmail.com",
#     "name": "testingworld",
#     "number": "+91-8743-913121"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.31.0",
#     "X-Amzn-Trace-Id": "Root=1-65a11d4a-3a15a3c56480d770194c2381"
#   },
#   "origin": "49.207.224.38",
#   "url": "https://httpbin.org/get?name=testingworld&email=testingworldindia%40gmail.com&number=%2B91-8743-913121"
# }
