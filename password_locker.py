PASSWORDS = {"email": "YOUR_PASSWORD",
             "facebook": "YOUR_PASSWORD",
             "twitter": "YOUR_PASSWORD"}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: python file.py [account] 🐍")
    sys.exit()
    
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for '{account}' copied to clipboard 😁")
else:
    print("There is no account named '{account}' 😭")
