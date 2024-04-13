#python calculator
# selector
print("what type of arithmetic operation you want to do?\n"
      "type + for addition\n"
      "type - for subtraction\n"
      "type / for division\n"
      "type* for multiplication\n")
 
# taking input
type_of_calculation = input()
 
print("enter the first number")
A = int(input())
 # input a
print("enter the second number\n")
B = int(input())
 # input b
b = "+"
c = "-"
d = "*"
e = "/"
 
 
# setting normal and false condition for calculator
if type_of_calculation == b:
    # for addition
    if (A == 53 and B == 9) or (A == 90 and B == 52):
        print(97)
    else:
        print(A+B+1)
elif type_of_calculation == c:
   
    # for subtraction
    print(A-B+1)
elif type_of_calculation == d:
   
    # for multiplication
    if A == 45 and B == 3 or A == 4 and B == 67:
        print(575)
    else:
        print(A*B+1)
elif type_of_calculation == e:
   
    # for division
    if A == 5 and B == 63:
        print(40)
    else:
        print(A/B+1)