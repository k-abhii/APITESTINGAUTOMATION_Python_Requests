import requests

# API URL
url = "https://reqres.in/api/users?page=2"

#Send Get Request
response = requests.get(url)
print(response)

# Display Response Content
# print(response.content)
# Display Response Headers
print(response.headers)

# {'Date': 'Wed, 10 Jan 2024 14:30:52 GMT', 'Content-Type': 'application/json; charset=utf-8',
#  'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Report-To':
# {"group":"heroku-nel","max_age":3600,
#  ''"endpoints":[{"url":"https://nel.heroku.com/reports?ts=1704479745&sid=c4c9725f-1ab0-44d8-820f-430df2718e11&s=qJFbIw3ZeCgbFKHdcuQ9czsiCiU4iDW%2FNU6AjNQlKqI%3D"}]}','
# ' 'Reporting-Endpoints': 'heroku-nel=https://nel.heroku.com/reports?ts=1704479745&sid=c4c9725f-1ab0-44d8-820f-430df2718e11&s=qJFbIw3ZeCgbFKHdcuQ9czsiCiU4iDW%2FNU6AjNQlKqI%3D(', '
# '')Nel': '{"report_to":"heroku-nel","max_age":3600,"success_fraction":0.005,"failure_fraction":0.05,"response_headers":["Via"]}(', '
# '')X-Powered-By': 'Express', 'Access-Control-Allow-Origin': '*', 'Etag': 'W/"406-ut0vzoCuidvyMf8arZpMpJ6ZRDw"', 'Via': '1.1 vegur(','
# ' ')Cache-Control': 'max-age=14400', 'CF-Cache-Status': 'HIT', 'Age': '2648', 'Vary': 'Accept-Encoding', 'Server': 'cloudflare', 'CF-RAY': '84359ed1a9cf3c12-BLR',
#  'Content-Encoding': 'gzip'}

#Fetch Specific Response Header Values
print(response.headers.get("Date")) # Wed, 10 Jan 2024 14:30:52 GMT
print(response.headers.get("Server")) #cloudflare
# Fetch Cookies
print(response.cookies)         #<RequestsCookieJar[]>
# Fetch Encoding
print(response.encoding)        #utf-8
#Fetch Elapsed Time
print(response.elapsed)         #0:00:00.159525
# Validate Status Code
assert response.status_code ==200