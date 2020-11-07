import requests

url = "http://www.example.com"
cookies = {"session": "asdfasdf12341234"}

response = requests.get(url, cookies=cookies)

print(response.text)
print(response.cookies)
# cool it worked
