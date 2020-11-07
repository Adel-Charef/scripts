import requests

urls = open("urls.txt", "r")
for url in urls:
    url = url.strip()
    req = requests.get(url)
    print(url, "report: ")
    try:
        xss_protect = req.headers['X-XSS-Protection']
        if xss_protect != "1; mode=block":
            print("X-XSS-Protection not set properly, XSS may be possible: ", xss_protect)
    except:
        print("X-XSS-Protection not set, XSS may be possible")
    try:
        content_type = req.headers['X-Content-Type-Options']
        if content_type != "nosniff":
            print("X-Content-Type-Options not set properly:", content_type)
    except:
        print("X-Content-Type-Options not set")
    try:
        csp = req.headers['Content-Security-Policy']
        print("Content-Security-Policy set:", csp)
    except:
        print("Content-Security-Policy missing")
    print("--------")
