#Write a program that will convert degrees celsius to degrees fahrenheit.

query = input("enter if you would like to convert celcius to farenheit or vice versa: ")
if query == "celcius":
    print("enter your current tempurature in celcius: ")
    celcius = float(input())
    farenheit = (celcius * 9/5) + 32
    print("your tempurature in farenheit is ", farenheit)
else:
    print("enter your current tempurature in farenheit: ")
    farenheit = float(input())
    celcius = (farenheit - 32) * 5/9
    print("your tempurature in celcius is", celcius)