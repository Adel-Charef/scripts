import requests
# finger print through headers

req = requests.get("http://packtpub.com")

headers = ["Server", "Date", "Via", "X-Powered-By", "X-Country-Code"]
for header in headers:
    try:
        result = req.headers[header]
        print("%s : %s" % (header, result))
    except:
        print("%s : Not Found" % header)


