#It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. 
#If you go on a wonderful holiday leaving on day number 3 (a Wednesday) 
#and you return home after 10 nights you would return home on a Saturday (day 6) 
#Write a general version of the program which asks for the starting day number, 
#and the length of your stay, 
#and it will tell you the number of day of the week you will return on.

start_day = int(input("Starting day (0=Sun, 6=Sat): "))# Ask for starting day (0=Sun, 6=Sat)
num_nights = int(input("Number of nights: "))# Ask for length of stay
return_day = (start_day + num_nights) % 7# Calculate return day
print("You will return on day", return_day)# Print
return_week = return_day  / 7
