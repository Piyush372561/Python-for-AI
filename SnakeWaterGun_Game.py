'''
1 for Snake 
-1 for Water 
0 for Gun
'''
import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {
    "Snake" : 1,
    "Water" : -1,
    "Gun" : 0,
}
reverseDict = {
    1: "Snake",
    -1: "Water",
    0 : "Gun",
}

you = youDict[youstr]
print("You chose: ",reverseDict[you])
print("Computer chose: ", reverseDict[computer])

if(computer == you):
    print("It's a Draw")
else:
    if(computer == -1 and you == 1):
        print("You Win")
    elif(computer == -1 and you == 0):
        print("Computer Won")
    elif(computer == 1 and you == -1):
        print("Computer win")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 0 and you == -1):
        print("you win")
    elif(computer == 0 and you == 1):
        print("Computer Win.")
    else:
        print("Something went wrong!")
