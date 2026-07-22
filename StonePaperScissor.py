'''
Stone = "s"
Paper = "p"
Scissor = "sc"
'''
import random

opponent = random.choice(["s","p","sc"])
youstr = input("Enter your choice: ")
yourDict = {
    "Stone" : "s",
    "Paper" : "p",
    "Scissor" : "sc"
}

reverseDict = {
    "s" : "Stone",
    "p" : "Paper",
    "sc" : "Scissor"
}

you = yourDict[youstr]
print("You chose: ", reverseDict[you])
print("opponent choose: ",reverseDict[opponent])

if(opponent == you):
    print("It's a Draw")
else:
    if(opponent == "p" and you == "s"):
        print("opponent Win")
    elif(opponent == "p" and you == "sc"):
        print("you Won")
    elif(opponent == "s" and you == "p"):
        print("you win")
    elif(opponent == "s" and you == "sc"):
        print("Opponent win")
    elif(opponent == "sc" and you == "p"):
        print("Opponent win")
    elif(opponent == "sc" and you == "s"):
        print("you Win.")
    else:
        print("Something went wrong!")