import string
import secrets


def secure_password_gen(pass_length):
    password = ''.join((secrets.choice(string.ascii_letters) for i in range(pass_length)))
    return password


n = int(input('Enter length of password : '))
print('Password generated is :', secure_password_gen(n))
