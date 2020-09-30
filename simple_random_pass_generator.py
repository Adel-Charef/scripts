import string
import secrets


def secure_password_gen(pass_length):
    password = "".join((secrets.choice(string.ascii_letters)
                        for i in range(pass_length)))
    return password


pass_len = int(input('Enter length of password : '))
print('Password generated is :', secure_password_gen(pass_len))
