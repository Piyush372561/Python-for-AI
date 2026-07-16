#Question-1
'''
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))

# 1.
greatest = num1
if  num2 > greatest:
    greatest = num2

if num3 > greatest:
    greatest = num3

if num4 > greatest:
    greatest = num4

print("Greatest no. among the four numbers: ", greatest)


#2
if num1>=num2 and num1>=num3 and num1>=num4:
    print(num1,"is the greatest no. among four of them.")
elif num2>=num1 and num2>=num3 and num2>=num4:
    print(num2,"is the greatest no. among four of them.")
elif num3>=num1 and num3>=num2 and num3>=num4:
    print(num3,"is the greatest no. among four of them.")
else:
    print(num4, "is the greatest no. among the four numbers.")

    
#3 - Ye built in function haio python mein jo greatest of number deta hai 
print(max(num1, num2, num3, num4))

#Question-2
Maths = int(input("Enter marks: "))
Physics = int(input("Enter marks: "))
Chemistry = int(input("Enter marks: "))
 
Percent = (Maths + Physics + Chemistry)/3
print(Percent)

if (Percent>=40):
    if Maths >= 33 and Physics>=33 and Chemistry>=33:
        print("Pass")
    else:
        print("Fail")
else:
    print("Fail")


#Question-3
text = input("Enter your text: ")

#this will always return This is a spam.
if "subscribe this" in text:
    print("This is a spam.")
if "buy now" in text:
    print("This is a spam.")
if "Click this" in text:
    print("This is a spam.")
if "make a lot of money" in text:
    print("This is a spam.")

#2.this will always return This is a spam.
if "subscribe this" or "buy now" or "click this" or "make a lot of money" in text:
    print("This is a spam.")

#3. approach
text = input("Enter your text: ")

if "subscribe this" in text or "buy now" in text or "click this" in text or "make a lot of money" in text:
    print("This is a spam.")
else: 
    print("This is not a spam")


#Question-4
User_name = input("Enter your name: ")

character = len(User_name)
print("No. of characters in User_name: ",character)

if character<10:
    print("Yes")
else:
    print("No")

    
#Question-5
l1 = ["Ajay", "Seema", "Piyush", "Lakshya"]
name = input("Enter name:")

if name in l1:
    print("Yes")
else:
    print("No")

'''

#Question-6
Marks = int(input("Enter marks: "))

if (Marks>=90) and (Marks<=100):
    print("Excellent")
elif (Marks>=80) and (Marks<90):
    print("A")
elif (Marks>=70) and (Marks<80):
    print("B")
elif (Marks>=60) and (Marks<70):
    print("C")
elif (Marks>=50) and (Marks<60):
    print("D")
else:
    print("F")

#Question-7
Post = input("Enter your post: ")

if "piyush" in Post:
    print("The post is talking about Piyush")
else:
    print("No")
