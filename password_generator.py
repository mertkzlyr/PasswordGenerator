import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
user_letters= int(input("How many letters would you like in your password?\n")) 
user_symbols = int(input("How many symbols would you like?\n"))
user_numbers = int(input("How many numbers would you like?\n"))

password_list = []
for letter in range(user_letters + 1):
  password_list.append(random.choice(letters))

for num in range(user_numbers + 1):
  password_list.append(random.choice(numbers))

for sym in range(user_symbols + 1):
  password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

pyperclip.copy(password)

print("Password generated! --->",password, "\nGenerated password copied to clipboard.")
