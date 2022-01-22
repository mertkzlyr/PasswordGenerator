import string
import secrets
import pyperclip

pass_lenght = input("How many characters do you want in your password? (default 20 for strong password)\n")
pass_lenght = 20 if pass_lenght == '' else int(pass_lenght)

alphabet = string.digits + string.ascii_letters + string.punctuation

while True:
    password = ''.join(secrets.choice(alphabet) for i in range(pass_lenght))
    if  any(char.islower() for char in password):
        any(char.isupper() for char in password)
        sum(char.isdigit() for char in password)
        break

pyperclip.copy(password)

print("Password generated! --->",password, "\nGenerated password copied to clipboard.")