import random
import string

print("Welcome to the hub! You have three options, a password generator, playing mad libs, or playing rock, paper, scissors, lizard, spock. Which one do you want to play?")

choice = input("Type 'password' to create a password or 'Mad Libs' to play Mad Libs, or 'Rock, Paper, Scissors, Lizard, Spock' to play Rock, Paper, Scissors, Lizard, Spock: ")


if choice == "password":
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
    print("Here is your new and generated password:", password)
    print(" ")

elif choice == "Mad Libs":
    print("Welcome to Mad Libs!")
    storymode = input("Which madlib would you like to play? 1, 2, or 3: ")
    if storymode == "1":
        noun1 = input("Enter a noun: ")
        noun2 = input("Enter another noun: ")
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter another adjective: ")
        verb1 = input("Enter a verb: ")
        verb2 = input("Enter another verb: ")
        if verb1 != type(string) or verb2 != type(string) or noun1 != type(string) or noun2 != type(string) or adjective1 != type(string) or adjective2 != type(string):
            print("You must enter text for all of the prompts!")
            exit(0)
        story = "Once upon a time there was a " + adjective1 + " " + noun1 + " who loved to " + verb1 + ". The " + noun1 + " wanted to " + verb2 + " the " + adjective2 + " " + noun2 + ", So the " + noun1 + " " + verb1 +" over to the " + noun2 + " and they " + verb2 + " all day long."

    elif storymode == "2":
        noun1 = input("Enter a noun: ")
        noun2 = input("Enter another noun: ")
        adjective1 = input("Enter an adjective: ")
        adjective2 = input("Enter another adjective: ")
        verb1 = input("Enter a verb: ")
        verb2 = input("Enter another verb: ")
        pronoun1 = input("Enter a name for your character:")
        story = "Once upon a time, there was a " + adjective1 + " " + noun1 + " who's name was " + pronoun1 + ", " + pronoun1 + " loved to " + verb1 + ". " + pronoun1 + " wanted to " + verb2 + " the " + adjective2 + " " + noun2 + ". So the " + noun1 + " " + verb1 + " over to the " + noun2 + " and they " + verb2 + " until their parents called them and yelled at them for being home too late."

    else:
        noun1 = input("Enter a date: ")
        name1 = input("Enter a name: ")
        adjective1 = input("Enter an adjective: ")
        noun2 = input("Enter a noun: ")
        story = "EXCUSED " + noun1 + ": please excuse " + name1 + ", who is far too " + adjective1 + " to be allowed to go to " + noun2 + " class."


    print(" ")
    print(story)
    print(" ")
    print("Thanks for playing Mad Libs!")
    print(" ")
    print(" ")

elif choice == "Rock, Paper, Scissors, Lizard, Spock":
    user_threw = input("What do you want to throw - rock, paper, scissors, lizard, or spock? ")
    if (
        (user_threw == "rock") 
        or (user_threw == "paper")
        or (user_threw == "scissors")
        or (user_threw == "spock")
        or (user_threw == "lizard")
    ):
        print(user_threw +' works')
    else:
        print(user_threw + "???? That doesn't work!?")
        exit(0)
    computer_threw = random.choice(["scissors","rock","paper", "lizard", "spock"])
    print("Computer chose " + computer_threw)
    if (computer_threw == user_threw):
        print("It's a tie!")
    elif (
        (computer_threw == "rock" and user_threw == "paper")
        or (computer_threw == "sciossors" and user_threw == "rock")
        or (computer_threw == "paper" and user_threw == "scissors")
        or (computer_threw == "spock" and user_threw == "lizard")
        or (computer_threw == "scissors" and user_threw == "spock")
        or (computer_threw == "rock" and user_threw == "spock")
        or (computer_threw == "lizard" and user_threw == "scissors")
        or (computer_threw == "lizard" and user_threw == "rock")
        or (computer_threw == "spock" and user_threw == "paper")
        or (computer_threw == "paper"  and user_threw == "lizard")
        ):
        print("Good job!  You beat the computer!")    
    else:
        print("The computer won!")