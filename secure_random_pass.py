# Let's mess around with secrets module
import secrets
import string

# Making a random secure password
def securePassword():
    stringSource = string.ascii_letters + string.digits + string.punctuation
    password = secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.punctuation)

    for i in range(10):
        password += secrets.choice(stringSource)

    char_list = list(password)
    secrets.SystemRandom().shuffle(char_list)
    password = "".join(char_list)
    print(f"Your Random Secure Password is: {password}")


# Making a random secure token
def secureToken():
    print("URL Example: https://example.com/user/adel/rest=")
    secure_url = input("Enter URL: ")
    secure_url += secrets.token_urlsafe(32)
    print(secure_url)


while True:
    choice = input('''What do you want ?
        * [1]: Random Secure Password
        * [2]: Random Secure Token
        * [0]: Quit
Enter your choice: ''')
    if choice == "1":
        securePassword()
        break
    elif choice == "2":
        secureToken()
        break
    elif choice == "0":
        break
    else:
        print("Invalid Input!!")
        continue
