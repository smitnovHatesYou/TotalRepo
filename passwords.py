import random
import string

print("Welcome to the random password generator!")

length = int(input("How long would you like the password to be? in characters: "))

include_lowercase = input("Include lowercase letters? (y/n) ").lower() == 'y'
include_uppercase = input("Include uppercase letters? (y/n) ").lower() == 'y'  
include_numbers = input("Include numbers? (y/n) ").lower() == 'y'
include_symbols = input("Include symbols? (y/n) ").lower() == 'y'

characters = ""

if include_lowercase:
  characters += string.ascii_lowercase

if include_uppercase:
  characters += string.ascii_uppercase  

if include_numbers:
  characters += string.digits

if include_symbols:
  characters += string.punctuation

password = "".join(random.choice(characters) for i in range(length))

print(" ")
print("Generated password:", password)
print(" ")