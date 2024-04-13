import random
user_threw = input("What do you want to throw - rock, paper, scissors, lizard, or spock? ")
print(user_threw)
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