import requests

req = requests.get("http://www.packtpub.com")
for cookie in req.cookies:
    print("Name:", cookie.name)
    print("Value:", cookie.value)
    if not cookie.secure:
        cookie.secure = "\x1b[31mFalse\x1b[39;49m"
        print("Secure:", cookie.secure)
    if "httponly" in cookie._rest.keys():
        cookie.httponly = "True"
    if cookie.domain_initial_dot:
        cookie.domain_initial_dot = "\x1b[31mTrue\x1b[39;49m"
        print("Loosly defined domain:", cookie.domain_initial_dot, '\n')
    else:
        cookie.httponly = "\x1b[31mFalse\x1b[39;49m"
        print('HTTPOnly:', cookie.httponly)
