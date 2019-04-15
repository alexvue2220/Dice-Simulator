import sys
from random import *

## prompting The user.
print("welcome to dice roll")
print("want to play?")
print("yes or no")

## userinput
userinput = input (': ')[0].lower()
print(userinput)

## ensure correct userinput
while userinput not in ["y","n"]:
    print("please answer yes or no")
    userinput = input (': ')[0].lower()
    print(userinput)

else:
    ##running simulator and prompting for user input.
    while userinput == "y":
        x = randint(1, 6)
        print("You rolled a {}".format(x))
        print("Want to roll agian?")
        print("yes or no")
        userinput = input (': ')[0].lower()

## ending the simulator
if userinput == "n" or "no":
    exit()