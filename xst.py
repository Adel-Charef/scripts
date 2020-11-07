import requests

# Cross Site Tracing vulnerability

methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'TEST']

for method in methods:
  req = requests.request(method, "http://packtpub.com")
  print(method, req.status_code, req.reason)
  if method == "TRACE" and 'TRACE / HTTP/1.1' in req.text:
    print("Possible Cross Site Tracing vulnerability Found!!")


