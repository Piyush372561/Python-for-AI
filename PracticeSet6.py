#Question-1
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))

# 1.
'''greatest = num1
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
'''
    
#3 - Ye built in function haio python mein jo greatest of number deta hai 
print(max(num1, num2, num3, num4))